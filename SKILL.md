---
name: house-skills-kit
description: 房产AI技能仓库总览：一仓多Skill，按身份分技能（房开企业/经纪公司/渠道分销/购房者业主/二手经纪人/一手销售/房产自媒体）。含公共计算工具包（房贷/二手房全成本/一手房成本/楼层折扣，35城规则库）与品牌顾问技能生成骨架（4类角色原型×29业务模块）。Use when 需要房产相关AI技能的安装、生成或按身份选型。
license: Apache-2.0
---

# house-skills-kit · 房产 AI 技能仓库

一仓多 Skill，按身份取用。本文件是仓库总览；各技能在 `skills/` 子目录下，都是独立完整的技能。

## 技能索引

| 技能 | 路径 | 适合谁 |
|---|---|---|
| **calc-toolkit 公共计算工具包** | `skills/calc-toolkit/` | 全身份：房贷月供、二手房交易全成本、一手房交易成本、楼层差价折扣。35 城规则库，四层引擎每个数字可追溯 |
| 购房顾问（排期） | `skills/`（待建） | 购房客户：资格/选筹/谈判 |
| 案场销售顾问（排期） | `skills/`（待建） | 房开案场 |
| 经纪人作业助手（排期） | `skills/`（待建） | 二手经纪人 |
| 渠道管理助手（排期） | `skills/`（待建） | 渠道分销 |

## 两条生产线

1. **`skills/` 直发技能**：独立 SKILL.md，直接发布 ClawHub（现有 1 个）。
2. **`template/` 品牌生成骨架**：4 类角色原型（consumer-buy / developer-sales / brokerage-agent / channel-distributor）× 29 业务模块，`python3 render.py --config brand.yaml --out output/my-brand/` 一份配置生成品牌专属顾问技能，`install.sh` 装进任意 Agent。

## 身份多了之后

按身份拆多仓（房开企业仓/经纪公司仓/购房者仓…），本仓保留公共计算工具包与骨架。当前阶段一仓管理，发布时各 Skill 独立成技能。
