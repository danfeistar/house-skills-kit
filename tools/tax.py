#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具02 · 二手房税费计算器（契税/增值税/个税：满二满五、首套二套、面积段）
清单序号：⑦-2｜规则来源：tools/rules/cities.yaml（三层引擎）
用法示例：
  python3 tax.py --price 1500000 --area 89 --city 昆明 --first 1 --held 6 --unique 1
  python3 tax.py --price 2000000 --area 120 --city 武汉 --first 2 --held 1 --orig 1600000
参数说明：
  --price  网签/成交价（元）        --area  建筑面积（㎡）
  --first  1=家庭首套 2=二套 3=三套及以上
  --held   满几年（0-2内填实际年限，≥2视为满二，≥5视为满五）
  --unique 1=卖方家庭唯一住房（配合满五免个税）
  --orig   原值（元，选填：用于差额个税对比展示）
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruleengine import get_rules, fmt_provenance, COMPLIANCE  # noqa: E402

W = lambda x: f"{x:,.0f}"


def main():
    ap = argparse.ArgumentParser(description="二手房税费计算器（⑦-2）")
    ap.add_argument("--price", type=float, required=True)
    ap.add_argument("--area", type=float, required=True)
    ap.add_argument("--first", type=int, default=1, choices=[1, 2, 3])
    ap.add_argument("--held", type=float, default=0)
    ap.add_argument("--unique", type=int, default=0)
    ap.add_argument("--orig", type=float, default=0)
    ap.add_argument("--city"); ap.add_argument("--district")
    ap.add_argument("--template")
    args = ap.parse_args()

    rules, prov = get_rules("tax", args.city, args.district, args.template)
    P, A = args.price, args.area
    lines = [f"＝ 二手房税费试算 ｜ 成交价 {W(P)} 元 ｜ {A:g}㎡ ｜"
             f" {'首套' if args.first==1 else '二套' if args.first==2 else '三套及以上'}"
             f" ｜ 满{'五' if args.held>=5 else '二' if args.held>=2 else '未满二'}"
             f"{'·家庭唯一' if args.unique else ''}"
             f"{' ｜ 城市:'+args.city if args.city else ' ｜ 全国默认档'}"
             f"{'/'+args.district if args.district else ''}", "─"*56]

    items = []

    # ── 契税（买方）── 2024年16号公告：140㎡线，首二套≤140㎡均1%
    deed = rules["deed_tax"]
    if args.first == 1:
        rate = deed["first_140le"] if A <= 140 else deed["first_140gt"]
        basis = f"首套{'≤140㎡' if A <= 140 else '>140㎡'}"
    elif args.first == 2:
        rate = deed["second_140le"] if A <= 140 else deed["second_140gt"]
        basis = f"二套{'≤140㎡' if A <= 140 else '>140㎡'}"
    else:
        rate = deed["third_plus"]
        basis = "三套及以上"
    deed_tax = P * rate
    items.append((f"契税（买方，{basis}，{rate*100:g}%）", deed_tax))

    # ── 增值税及附加（卖方）── 2025年17号公告：满2年免，未满2年3%含税换算
    if args.held >= 2:
        vat, extra, vat_note = 0.0, 0.0, "满2年免征（全国统一，含北上广深）"
    else:
        vat_rate = rules["vat_rate"]
        price_in = rules.get("vat_price_in", 1)
        vat_net = P / (1 + vat_rate) if price_in else P
        vat = vat_net * vat_rate
        extra = vat * rules.get("vat_extra_rate", 0.0)
        vat_note = f"未满2年 3%征收率（含税换算）"
    items.append((f"增值税（卖方，{vat_note}）", vat))
    if extra > 0:
        items.append(("  ↳ 附加税费（增值税额×12%）", extra))

    # ── 个税（卖方）──
    if args.held >= 5 and args.unique:
        indiv, indiv_note = 0.0, "满五唯一免征"
    else:
        it = rules["indiv_tax"]
        normal = P * it["normal"]
        if args.orig and P > args.orig:
            diff_tax = (P - args.orig) * 0.20
            indiv = min(normal, diff_tax)
            indiv_note = f"全额{it['normal']*100:g}%={W(normal)} 与 差额20%={W(diff_tax)} 取低"
        else:
            indiv = normal
            indiv_note = f"全额{it['normal']*100:g}%（未提供原值/未满五唯一）"
    items.append((f"个税（卖方，{indiv_note}）", indiv))

    total = sum(v for _, v in items)
    for name, v in items:
        lines.append(f"  · {name}：{W(v)} 元")
    lines.append("─" * 56)
    lines.append(f"  合计税费 ≈ {W(total)} 元（占房价 {total/P*100:.2f}%）")
    buyer = deed_tax
    lines.append(f"  · 买方承担 {W(buyer)} 元；卖方承担 {W(total-buyer)} 元（实际谁承担以谈判为准，交易习惯多为买方包税）")

    lines.append("")
    lines.append(fmt_provenance(prov, ["deed_tax", "vat_rate", "vat_extra", "indiv_tax"]))
    lines.append("")
    lines.append("口诀提醒：满二免增值税（全国统一），满五唯一再免个税；首二套140㎡内契税均1%。")
    lines.append(COMPLIANCE)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
