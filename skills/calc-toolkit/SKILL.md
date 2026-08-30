---
name: house-calc-toolkit
description: 房产公共计算工具包：房贷月供（组合贷/等额本息本金）、二手房交易全成本（税4项+费6项买卖分账）、一手房交易成本（契税/维修基金/首年物业/登记工本费）、楼层差价与折扣叠加。全国35城规则库三层引擎（全国默认→城市/区县→我的模板）+--set即时覆盖，每个数字带来源可追溯。Use when 用户问房贷月供、买房税费、新房交房费用、楼层差价或折扣叠加测算。
license: Apache-2.0
---

# house-calc-toolkit · 房产公共计算工具包

零依赖 Python 工具（任何电脑有 Python3 即可跑），服务所有身份端：购房者、经纪人、案场销售、渠道、自媒体博主的算数场景。

## 快速上手

```bash
python3 skills/calc-toolkit/mortgage.py --price 1500000 --downpay 30 --years 30 --city 昆明
python3 skills/calc-toolkit/tax.py --price 1500000 --area 89 --city 昆明 --first 1 --held 6 --unique 1   # 二手全成本
python3 skills/calc-toolkit/newhome.py --price 1500000 --area 100 --city 昆明 --first 1                  # 一手全成本
python3 skills/calc-toolkit/floor.py --price 25000 --area 100 --floor 15 --top 30 --floor-adj 300 --d 98 --d 99 --pay one_time
```

## 工具清单（4/20）

| # | 工具 | 脚本 | 场景 |
|---|---|---|---|
| ⑦-1 | 房贷月供计算器 | `mortgage.py` | 商贷/公积金/组合贷 × 等额本息/本金，利息对比、首付档校验 |
| ⑦-2 | 二手房交易全成本测算 | `tax.py` | 税4项（契税/增值税及附加/个税/印花税）+ 费6项（中介2%/交易手续费/登记/评估/赎楼/土地收益金），买卖分账 |
| ⑦-6 | 一手房交易成本测算 | `newhome.py` | 契税140㎡线 + 维修基金（物业类型三档×城市档：昆明高层90、佛山南海85/91/107）+ 首年物业预存 + 不动产登记工本费 |
| ⑦-15 | 楼层差价+折扣叠加 | `floor.py` | 楼层加价 × 折上折 × 付款折扣，折扣真伪校验（防"先涨后折"） |

## 规则四层引擎（每个数字可追溯）

```
层1 全国默认档（rules/cities.yaml → default）
      ↓ 被覆盖
层2 城市档（35城）→ 区县档（districts）
      ↓ 被覆盖
层3 我的模板（--save-template / --template）
      ↓ 被覆盖
层4 --set 即时覆盖（任何参数当场改，来源表如实标注）
```

- 未内置城市：自动套全国默认档并明确提示（不装懂）
- 每项输出末尾附「参数来源表」：这个数字来自哪个城市档、哪个时点
- 政策变了只改 `rules/cities.yaml`，工具代码不动

详细说明见包内 `README.md`。
