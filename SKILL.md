---
name: house-skills-kit
description: 房产AI技能仓库总览：按身份分技能（房开企业/经纪公司/渠道分销/购房者业主/二手经纪人/一手销售/房产自媒体）。已发布calc-toolkit公共计算工具包与案场销售线五技能（话术库/异议处理/算价逼定/接待挖掘/判客跟进）（19件收官：房贷月供/二手房全成本/一手房成本/购房能力/提前还款/首套二套认定/楼层折扣/公积金额度/佣金提成/得房率换算/租金回报/LPR变动影响/持有成本/买房vs理财/面积误差补退/违约金定金/房龄贷款年限/楼面价货值/日照楼间距，35城规则库四层引擎，每个数字可追溯）；template/为品牌顾问技能生成骨架（4类角色原型×29业务模块）。Use when 需要房产相关AI技能的安装、使用、生成或按身份选型。
license: Apache-2.0
---

# house-skills-kit · 房产 AI 技能仓库

按身份分 Skill，按需取用。本文件是仓库总览；各技能在 `skills/` 子目录下，均为独立完整技能（自带 SKILL.md，可单独发布安装）。

## 技能索引

| 技能 | 路径 | 适合谁 |
|---|---|---|
| **calc-toolkit 公共计算工具包** | `skills/calc-toolkit/` | 全身份：12 件工具——房贷月供、二手房交易全成本、一手房交易成本、购房能力、提前还款、首套二套认定、楼层折扣、公积金额度、佣金提成、得房率换算、租金回报、LPR变动影响。35 城规则库四层引擎，每个数字可追溯，全参数 `--set` 可覆盖 |
| **sales-talk-library 案场话术库** | `skills/sales-talk-library/` | 置业顾问/销售经理：地段/配套/户型/竞品/品牌五域标准说辞、分客群变通与合规红线 |
| **sales-objection-handling 客户异议处理** | `skills/sales-objection-handling/` | 置业顾问/销售经理：高频异议三段式应对、禁语清单与演练 |
| **sales-closing-sop 算价与逼定 SOP** | `skills/sales-closing-sop/` | 置业顾问/销售主管：算价动作链、议价博弈、逼定信号与团队配合逼定 |
| **sales-reception-sop 接待与需求挖掘 SOP** | `skills/sales-reception-sop/` | 置业顾问/销售主管：首访接待动线、七维需求挖掘、匹配带看与交接 |
| **sales-lead-grading 判客与跟进 SOP** | `skills/sales-lead-grading/` | 置业顾问/销售主管：ABC判客分级、跟进节奏、掉客挽回与归属仲裁 |
| **sales-mortgage-sop 按揭问题应对 SOP** | `skills/sales-mortgage-sop/` | 置业顾问/按揭专员：资质预判分流、六类高频按揭问题路径与话术、合规红线 |
| **sales-opening-sop 开盘执行 SOP** | `skills/sales-opening-sop/` | 置业顾问/案场负责人/开盘执行团队：盘前梳理预登记、认筹转认购、开盘日七环节选房动线、规则口径、五类应急预案、盘后转化 |
| **presale-marketing-sop 蓄客期营销动作清单** | `skills/presale-marketing-sop/` | 策划/营销负责人/自媒体运营：节点倒排节奏、暖场/拓客/圈层/认筹预热动作库、自媒体蓄客专节（定位/日历/线索闭环）、四级漏斗复盘、合规红线 |
| **competitive-intel-sop 竞品踩盘与市场监控** | `skills/competitive-intel-sop/` | 策划/营销负责人/市调岗：竞品A/B/C分级、六模块现场采集、百分制打分与竞品预判、四指标周监控三源交叉、月度竞品报告、反踩盘纪律与合规红线 |
| **activity-organization-sop 营销活动组织 SOP** | `skills/activity-organization-sop/` | 策划/营销负责人/案场负责人：活动目标定义、活动选型矩阵、一页简报、预算审批、执行清单、线索承接与复盘闭环、合规红线 |
| **marketing-materials-sop 营销物料与示范区优化 SOP** | `skills/marketing-materials-sop/` | 策划/示范区负责人/置业顾问：物料任务分类、设计简报、信息与合规审核、示范区四层巡检、改进台账、版本管理与反馈复盘 |
| **engineering-progress-broadcast-sop 工程进度与品质播报 SOP** | `skills/engineering-progress-broadcast-sop/` | 工程部/策划/品牌/案场客服：工程资料采集、节点对照、品质工艺表达、延期沟通、敏感问题升级、发布检查与复盘归档 |
| **pricing-incentive-release-sop 价格策略与优惠释放 SOP** | `skills/pricing-incentive-release-sop/` | 营销负责人/案场负责人/置业顾问：价格事实核验、房源与客户分层、优惠梯度、审批变更、案场执行、台账复盘与合规红线 |
| **channel-collaboration-sop 渠道协同与分销管理 SOP** | `skills/channel-collaboration-sop/` | 渠道负责人/项目营销/案场/财务：渠道准入分层、政策培训、报备查重、带访交接、判客仲裁、佣金对账与渠道复盘 |
| **customer-advocacy-referral-sop 客户口碑与老带新运营 SOP** | `skills/customer-advocacy-referral-sop/` | 客户关系/营销/案场/内容：服务反馈分层、口碑内容授权、推荐触发、线索登记、权益兑现、客诉隔离与复盘 |
| 购房顾问（排期） | `skills/`（待建） | 购房客户：资格/选筹/谈判 |
| 案场销售顾问（排期） | `skills/`（待建） | 房开案场 |
| 经纪人作业助手（排期） | `skills/`（待建） | 二手经纪人 |
| 渠道管理助手（排期） | `skills/`（待建） | 渠道分销 |
| 内容创作助手（排期） | `skills/`（待建） | 房产自媒体 |

## 两条生产线

1. **`skills/` 直发技能**：独立 SKILL.md，发布 ClawHub 各自成技能（现有 calc-toolkit、sales-talk-library、sales-objection-handling、sales-closing-sop、sales-reception-sop、sales-lead-grading、sales-mortgage-sop、sales-opening-sop 八个）。
2. **`template/` 品牌生成骨架**：4 类角色原型（consumer-buy / developer-sales / brokerage-agent / channel-distributor）× 29 业务模块，`python3 render.py --config brand.yaml --out output/my-brand/` 一份配置生成品牌专属顾问技能，`install.sh` 装进任意 Agent。

## 使用顺序建议

测算场景按咨询流串用：**购房能力**（能买多少）→ **月供**（月供多少）→ **楼层折扣**（这套房折后价）→ **新房/二手成本**（交易税费）→ **提前还款**（买后规划）。

## 规则与数据

- 政策档位全部外置 `skills/calc-toolkit/rules/cities.yaml`（35 城，标注文号/口径/as_of），政策更新改配置不动代码
- 使用者可用 `--city` 选城市档、`--template` 挂自己的模板、`--set 键=值` 临时覆盖任意参数
- 所有档位默认为演示口径，正式经营使用前请按所在城市官方公告核对
