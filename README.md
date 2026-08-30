# house-skills-kit 🏠

**房产 AI 技能仓库：按身份分 Skill，按需取用。** 面向房开企业、经纪公司、渠道分销、购房者业主、二手经纪人、一手销售、房产自媒体博主等身份，每个身份场景一个独立 Skill，装哪个用哪个。

> 不绑定任何平台和数据源：模板通用，数据走开放适配器接口，接哪家数据商、装进哪个 Agent 都由你决定。

## 仓库结构：一仓多 Skill（身份多了再分仓）

```
house-skills-kit/
├── skills/                  ← 各身份 Skill（每个都是独立完整的技能，可单独发布）
│   └── calc-toolkit/        ← ①公共计算工具包（房贷/税费/新房成本/楼层折扣，全身份通用）
├── template/                ← 技能生成骨架（4类角色原型 × 29业务模块，渲染品牌专属技能）
├── examples/                ← 渲染示例
├── render.py / install.sh   ← 骨架配套工具
└── SKILL.md                 ← 仓库总览（入口）
```

**发布策略**：`skills/` 下每个子目录都是一个独立 Skill（有自己的 SKILL.md），发布到 ClawHub 时各自成技能；Git 仓库始终只有一个，后续 Skill 多了再按身份拆多仓（房开企业仓 / 经纪公司仓 / 购房者仓…）。

## 身份 → Skill 路线图

| 身份 | Skill | 状态 |
|---|---|---|
| 全身份通用 | `calc-toolkit` 公共计算工具包 | ✅ 已发布（4/20 工具，持续扩充） |
| 购房客户 | C端购房顾问（资格/选筹/谈判） | 排期 |
| 房开案场 | 案场销售顾问 | 排期 |
| 二手经纪人 | 经纪人作业助手 | 排期 |
| 渠道分销 | 渠道管理助手 | 排期 |
| 房产自媒体 | 内容创作助手 | 排期 |

（模板侧另有 4 类角色原型 × 29 业务模块的生成骨架，见下）

---

### 分发渠道

| 平台 | 链接 | 用途 |
|---|---|---|
| GitHub（主库） | [github.com/danfeistar/house-skills-kit](https://github.com/danfeistar/house-skills-kit) | 源仓库 · Issues · PR |
| Gitee 镜像 | [gitee.com/danfeistar/house-skills-kit](https://gitee.com/danfeistar/house-skills-kit) | 国内快速访问 |
| ClawHub 技能市场 | [clawhub.ai/skills/house-skills-kit](https://clawhub.ai/skills/house-skills-kit) | AI Agent 一键安装 |
| AtomGit（开源中国） | [atomgit.com/danfeistar/house-skills-kit](https://atomgit.com/danfeistar/house-skills-kit) | 开源中国生态 |

## 👤 作者

**老何** — 地产行业从业 17 年，历任多家房企云南营销负责人，长期深耕云南及昆明地产市场，早期 AI 使用者与运用者。
现正全力做「房产 AI 平台」（房企端 + 经纪公司端 + 销售人员端 + 买房客户端），专注把 AI 运用到中国更多的地产行业场景中。
本仓库的业务模块（判客规则 / 佣金政策 / 案场话术 / 验房清单 / 租赁红线…）全部来自一线业务实践和各类企业规范化工作场景，不是工程师想象出来的 prompt。

> 联系合作/交流：[GitHub 主页](https://github.com/danfeistar) · 欢迎 Issue 留言

---

## 快速开始（30 秒，零外部依赖）

> 🇨🇳 国内镜像：[Gitee](https://gitee.com/danfeistar/house-skills-kit)（码云，同步自 GitHub）

```bash
git clone https://github.com/danfeistar/house-skills-kit.git
cd house-skills-kit

# ① 公共计算工具包（全身份通用）
python3 skills/calc-toolkit/mortgage.py --price 1500000 --downpay 30 --years 30 --city 昆明
python3 skills/calc-toolkit/tax.py --price 1500000 --area 89 --city 昆明 --first 1 --held 6 --unique 1
python3 skills/calc-toolkit/newhome.py --price 1500000 --area 100 --city 昆明 --first 1

# ② 生成品牌专属顾问技能（模板骨架）
python3 render.py --config examples/kunming/kunming.buy.yaml --out output/my-brand/
```
