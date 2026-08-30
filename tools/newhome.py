#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具06 · 一手房（新房）交易成本测算器（契税+维修基金+首年物业+配套杂费）
清单序号：⑦-6｜规则来源：tools/rules/cities.yaml::newhome（三层引擎 + 层4 --set）
范围（老何 08-30 指示）：一手房与二手不同——维修基金、首年物业等相关费用都要涵盖；
买方口径为主：契税/维修基金/物业预存/燃气初装/登记费/贷款评估+抵押登记；可加装修/车位参考行。

用法示例：
  python3 newhome.py --price 1500000 --area 100 --city 昆明 --first 1
  python3 newhome.py --price 2600000 --area 128 --city 武汉 --first 2 --loan 1500000 --months 6
  python3 newhome.py --price 1500000 --area 100 --set repair_fund_per_area=90 --set property_fee=1.8
参数说明：
  --price 网签/合同价（元）  --area 建筑面积（㎡）  --first 1/2/3  --loan 贷款额（元）
  --months 交房预存物业费月数（默认读规则库）  --decor 装修预算（元，选填参考行）  --parking 车位价（元，选填参考行）
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruleengine import get_rules, fmt_provenance, COMPLIANCE  # noqa: E402

W = lambda x: f"{x:,.0f}"


def _num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


def main():
    ap = argparse.ArgumentParser(description="一手房交易成本测算器（⑦-6）")
    ap.add_argument("--price", type=float, required=True, help="网签/合同价（元）")
    ap.add_argument("--area", type=float, required=True, help="建筑面积（㎡）")
    ap.add_argument("--first", type=int, default=1, choices=[1, 2, 3])
    ap.add_argument("--loan", type=float, default=0, help="贷款额（元，>0 计评估+抵押登记）")
    ap.add_argument("--months", type=float, default=None, help="交房预存物业费月数（覆盖规则库）")
    ap.add_argument("--decor", type=float, default=0, help="装修预算（元，参考行，不计入必缴）")
    ap.add_argument("--parking", type=float, default=0, help="车位价（元，参考行，不计入必缴）")
    ap.add_argument("--city"); ap.add_argument("--district")
    ap.add_argument("--template")
    ap.add_argument("--set", action="append", default=[], metavar="KEY=VALUE",
                    help="即时覆盖任意规则参数，如 --set repair_fund_per_area=90")
    args = ap.parse_args()

    overrides = {}
    for kv in getattr(args, "set"):
        if "=" not in kv:
            ap.error(f"--set 需要 KEY=VALUE 格式：{kv}")
        k, v = kv.split("=", 1)
        overrides[k.strip()] = _num(v.strip())

    rules, prov = get_rules("newhome", args.city, args.district, args.template, overrides=overrides)
    tax_rules, _ = get_rules("tax", args.city, args.district, args.template, overrides=overrides)
    P, A = args.price, args.area
    month = args.months if args.months is not None else rules.get("prepaid_months", 12)

    def g(key, default):
        if key in rules:
            return rules[key]
        return rules.get(key, default)

    lines = [f"＝ 一手房交易成本试算 ｜ 合同价 {W(P)} 元 ｜ {A:g}㎡ ｜"
             f" {'首套' if args.first==1 else '二套' if args.first==2 else '三套及以上'}"
             f"{' ｜ 城市:'+args.city if args.city else ' ｜ 全国默认档'}"
             f"{'/'+args.district if args.district else ''}", "─"*56]

    must = []   # 必缴项 (名称, 金额, 依据说明)
    ref = []    # 参考项（装修/车位等，不计入必缴小计）

    # ── 契税（沿用二手同档：140㎡线 2024年16号公告）──
    deed = tax_rules["deed_tax"]
    if args.first == 1:
        rate = deed["first_140le"] if A <= 140 else deed["first_140gt"]
        basis = f"首套{'≤140㎡' if A <= 140 else '>140㎡'}"
    elif args.first == 2:
        rate = deed["second_140le"] if A <= 140 else deed["second_140gt"]
        basis = f"二套{'≤140㎡' if A <= 140 else '>140㎡'}"
    else:
        rate = deed["third_plus"]
        basis = "三套及以上"
    must.append((f"契税（{basis}，{rate*100:g}%）", P*rate, "与二手同档（140㎡线）"))

    # ── 住宅专项维修基金（交房前缴存，口径随城市）──
    if rules.get("repair_fund_mode") == "per_price":
        rf = P * rules.get("repair_fund_per_price", 0.0)
        rf_note = f"总价×{rules.get('repair_fund_per_price',0)*100:g}%"
    else:
        rfa = rules.get("repair_fund_per_area", 110)
        rf = A * rfa
        rf_note = f"{rfa:g} 元/㎡"
    must.append((f"住宅专项维修基金（{rf_note}，交房前缴存）", rf, "交房时一次性缴，入专项账户"))

    # ── 首年物业费（预存，月数可调）──
    pf = rules.get("property_fee", 2.5)
    prop = A * pf * month
    must.append((f"物业费预存（{pf:g} 元/㎡/月 × {month:g} 个月）", prop, "多数项目交房预存3-12个月"))

    # ── 燃气初装/开户（部分城市已含在房价）──
    gas = rules.get("gas_install", 0)
    if gas:
        must.append(("燃气初装/开户费", gas, "已含在房价的城市为0"))

    # ── 登记费 ──
    reg = rules.get("registration", 80)
    must.append((f"不动产登记费（{reg:g} 元/套）", reg, "住宅80元/套"))

    # ── 贷款两件套 ──
    if args.loan > 0:
        appr = rules.get("appraisal_rate", 0.001)
        must.append((f"贷款评估费（贷款额×{appr*100:g}%）", args.loan*appr, "商业贷款需评估"))
        mreg = rules.get("mortgage_reg", 80)
        must.append((f"抵押登记费（{mreg:g} 元/套）", mreg, "按揭登记"))

    # ── 参考项（不计必缴）──
    if args.decor:
        ref.append((f"装修预算（参考行）", args.decor))
    if args.parking:
        ref.append((f"车位（参考行，产权另计）", args.parking))

    # ── 汇总 ──
    for name, v, note in must:
        lines.append(f"  · {name}：{W(v)} 元 ｜ {note}")
    subtotal = sum(v for _, v, _ in must)
    lines.append("─" * 56)
    lines.append(f"  ★ 交房阶段一次性支出（必缴）≈ {W(subtotal)} 元"
                 f"（占房价 {subtotal/P*100:.2f}%）")
    if ref:
        for name, v in ref:
            lines.append(f"  · {name}：{W(v)} 元（不计入必缴）")
        lines.append(f"  含参考项合计 ≈ {W(subtotal + sum(v for _, v in ref))} 元")
    lines.append("")
    lines.append("  说明：一手房无增值税/个税（卖方是开发商，其税费在开发商环节）；"
                 "也没有中介费（渠道佣金由开发商支付）。")
    lines.append("  维修基金/物业费/燃气初装各城各项目差异大——每项都可 --set 覆盖，"
                 "以购房合同与交房公示为准。")

    lines.append("")
    keys = ["repair_fund_mode", "property_fee", "gas_install", "deed_tax"] + sorted(overrides.keys())
    lines.append(fmt_provenance(prov, [k for k in keys if k in prov]))
    lines.append(COMPLIANCE)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
