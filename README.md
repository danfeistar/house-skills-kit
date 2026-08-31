# house-skills-kit 🏠

**房产 AI 技能仓库 —— 按身份分 Skill，按需取用。**

为房地产行业的七类角色提供开箱即用的 AI 技能（Skill）：房开企业、经纪公司、渠道分销公司、购房者/业主、二手经纪人、一手销售人员、房产自媒体博主。每个身份场景对应一个独立 Skill，`skills/` 目录下各技能均含完整提示词与配套工具，可单独安装、单独发布。

> 🇨🇳 模板通用、零外部依赖（纯 Python 标准库）：不绑定任何平台与数据商，装进 Claude / 其他 Agent 均可。

## 已发布技能

### 🧮 calc-toolkit · 公共计算工具包（全身份通用）

一套覆盖房产交易核心测算场景的命令行工具，**全部身份共用**。

| 编号 | 工具 | 命令 | 说明 |
|---|---|---|---|
| ⑦-1 | 房贷月供 | `mortgage.py` | 商贷/公积金/组合贷 × 等额本息/本金，按城市利率档自动取数 |
| ⑦-2 | 二手房全成本 | `tax.py` | 契税/增值税/个税 + 中介/评估/担保等 6 项费用，买卖双方分账 |
| ⑦-3 | 提前还款 | `prepay.py` | 缩期 vs 减月供双方案对比，违约金/最低额提示，省息一目了然 |
| ⑦-5 | 购房能力 | `capacity.py` | 收入负债 → 可贷上限 → 可买总价，银行双线口径（月供收入比 × 首付成数），瓶颈诊断 |
| ⑦-6 | 一手房成本 | `newhome.py` | 契税/维修基金（按城市×物业类型）/首年物业/登记工本费，按功能分类出单 |
| ⑥ | 首套二套认定 | `status.py` | 商贷/公积金/契税三口径分判（认房不认贷），卖一买一，联动下游工具参数 |
| ⑦-15 | 楼层差价折扣 | `floor.py` | 楼层修正 × 营销折上折，防"先涨后折"真伪校验 |
| ⑦-16 | 公积金额度 | `fund.py` | 四限取最低：上限/房价成数/还贷能力/余额倍数×缴存时间系数，多子女/绿建/人才上浮，组合贷缺口提示 |

**35 城规则库**（北上广深 + 强二线 + 昆明等省会全覆盖）+ **四层规则引擎**：

```
全国默认档 → 城市档（如昆明高层维修基金90元/㎡）→ 区县档 → 我的模板档（使用者自建）
```

- 每个数字可追溯：输出带「参数来源」，规则档标注文号/口径（如"2024年契税16号公告：140㎡线"）
- 政策数据与代码分离：政策变了改 `rules/cities.yaml`，工具不用动
- 万能覆盖：任何参数均可 `--set 键=值` 即时改（如 `--set dti=0.55`）

**快速上手**（零安装，Python 3.8+ 直接跑）：

```bash
git clone https://github.com/danfeistar/house-skills-kit.git
cd house-skills-kit

python3 skills/calc-toolkit/mortgage.py --price 1500000 --downpay 30 --years 30 --city 昆明
python3 skills/calc-toolkit/capacity.py --income 8000,6000 --cash 400000 --debts 2000 --city 昆明
python3 skills/calc-toolkit/tax.py --price 1500000 --area 89 --city 昆明 --first 1 --held 6 --unique 1
python3 skills/calc-toolkit/prepay.py --loan 1000000 --rate 3.1 --years 30 --paid 24 --prepay 200000
```

## 技能路线图（按身份扩容）

| 身份 | Skill | 状态 |
|---|---|---|
| 全身份通用 | `calc-toolkit` 公共计算工具包 | ✅ 已发布（8 件工具，20 件锁版清单持续扩充） |
| 购房客户 | C端购房顾问（资格/选筹/谈判） | 排期 |
| 房开案场 | 案场销售顾问 | 排期 |
| 一手销售 | 置业顾问跟客助手（含判客/话术） | 排期 |
| 二手经纪人 | 经纪人作业助手 | 排期 |
| 渠道分销 | 渠道管理助手 | 排期 |
| 房产自媒体 | 内容创作助手 | 排期 |

## 两条生产线

1. **`skills/` 直发技能**：每个子目录独立 SKILL.md，发布到 ClawHub 各自成技能，可独立安装。
2. **`template/` 品牌生成骨架**：4 类角色原型（购房者/房开销售/经纪经纪人/渠道分销）× 29 业务模块，一份品牌配置即可生成专属顾问技能：

```bash
python3 render.py --config examples/kunming/kunming.buy.yaml --out output/my-brand/
```

## 分发渠道

| 平台 | 链接 |
|---|---|
| GitHub 主库 | [github.com/danfeistar/house-skills-kit](https://github.com/danfeistar/house-skills-kit) |
| Gitee 镜像 | [gitee.com/danfeistar/house-skills-kit](https://gitee.com/danfeistar/house-skills-kit) |
| AtomGit 镜像 | [atomgit.com/danfeistar/house-skills-kit](https://atomgit.com/danfeistar/house-skills-kit) |
| ClawHub 技能市场 | [clawhub.ai/skills/house-skills-kit](https://clawhub.ai/skills/house-skills-kit) |

## 👤 作者

**老何** — 地产行业从业 17 年，历任多家房企云南营销负责人，长期深耕云南及昆明市场，早期 AI 使用者与运用者。现全力建设「房产 AI 平台」（房企端 + 经纪公司端 + 销售人员端 + 买房客户端）。

**为什么做这个仓库**：作者在国内外公开渠道（GitHub / ClawHub / 各大 AI 应用市场）均未找到专注中国房地产的 AI Skill 工具库——市面上的 Skill 生态几乎空白于这个年交易额十万亿级的行业。既然没有，就来做**最早、最专业的中文房产 AI Skill 与工具库**：把一线地产人的业务知识，做成 AI 真正能用的技能。

**本仓库的差异化**：这里的业务模块（判客规则 / 佣金政策 / 案场话术 / 验房清单 / 城市税费档…）全部来自一线业务实践和企业规范化工作场景，不是工程师想象出来的 prompt。AI 懂技术，我们懂房产——两者结合才是行业真正能用的 AI 工作流。

> 💡 **免费开源，长期维护**。如果它对你的工作有帮助，欢迎 Star / Issue / 转发——每一次使用和反馈都是对"房产 AI 开源"路线的支持。
>
> 🤝 **业务合作**：需要为你的房企 / 经纪公司 / 销售团队定制 AI 工具与 AI 工作流？欢迎通过 [GitHub 主页](https://github.com/danfeistar) 联系作者——一线地产 17 年 × AI 工程化落地，帮你把 AI 真正用进业务。

## License

Apache-2.0
