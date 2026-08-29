# house-skills-kit 🏠

**一套开源的「房产 AI 顾问技能」生成骨架：任何房开商、中介机构、渠道公司、个人房产从业者，都能用一份配置生成自己品牌的 AI 顾问技能。**

> 框架逻辑参照社区 Skill 分发最佳实践与头部平台公开的方法论骨架（顾问式服务流程），全部正文为原创重写；数据层通过开放适配器接口解耦，不依赖任何闭源组件。

---

## 👤 作者

**老何** — 地产行业 10+ 年，深耕昆明市场。
正在做「昆明房产 AI 工具平台」（经纪人端 + 买房者端），专注把 AI 真正装进中国地产企业的日常工作流。
本仓库的 29 个业务模块（判客规则/佣金政策/案场话术/验房清单/租赁红线…）全部来自一线业务实践，不是工程师想象出来的 prompt。

> 联系合作/交流：[GitHub 主页](https://github.com/danfeistar) · 欢迎 Issue 留言

---

## 快速开始（30 秒，零外部依赖）

```bash
git clone https://github.com/<you>/house-skills-kit.git
cd house-skills-kit
pip install pyyaml          # 唯一依赖
python3 render.py --config examples/kunming/kunming.buy.yaml --out output/
# → output/kunming-buy/SKILL.md + manifest.json，装进你的 Agent 即用
```

## 核心设计：角色原型 + 挂载模块

不同角色要的不是同一个助手，所以骨架按**四类角色原型**出模板，再按需**挂载增值模块**：

### 四类角色原型（archetype）

| 原型 | 服务对象 | 对应场景 |
|---|---|---|
| `consumer-buy` | 购房客户 | 平台/经纪公司的C端买房咨询顾问 |
| `developer-sales` | 购房客户 | 开发商案场AI置业顾问（留资→到访→认筹→签约五阶推进） |
| `brokerage-agent` | 经纪人本人 | 经纪人B端作业助手（画像/筛房/讲房/跟进提效） |
| `channel-distributor` | 渠道/分销伙伴 | 渠道作业助手（速览卡/报备三查/结佣四要素） |

### 增值模块（29 个 modules，中文房产全场景，按企业类型分组，均可独立挂载）

**C端 / 平台型**：`estate-review` 楼盘七维评测 · `ad-compliance` 广告合规检查 · `loan-calc` 贷款税费计算 · `policy-qa` 购房资格问答 · `content-marketing` 内容获客 · `rent-advisor` 租房顾问与防坑 · `landlord-mgmt` 房东租赁管理 · `handover-inspection` 交付验房 · `commercial-invest` 商铺投资测算 · `urban-renewal` 旧改拆迁问答 · `property-community` 物业与社区生活

**中介机构**：`listing-audit` 实勘助手 · `listing-inventory` 房源全生命周期管理（分级/调价建议） · `client-crm` 客户管理（ABC分级/流转/保护） · `match-engine` 意向匹配引擎（可解释匹配+反馈闭环） · `customer-followup` 跟进节奏 · `negotiation-coach` 议价辅导 · `transaction-compliance` 交易风控四道检查点

**渠道公司**：`channel-mgmt` 分销渠道管理（准入/分层/健康度） · `inner-attribution` 内部渠道精准判客（时间戳/保护期/仲裁） · `commission-mgmt` 佣金政策管理（六要素政策库/版本回溯/结佣对账） · `sub-brokerage-mgmt` 下属中介公司信息管理（资质预警/信息下达回收） · `performance-monitor` 业绩监控与评估（漏斗口径/归因卡/评估支持） · `partner-training` 伙伴培训 · `policy-briefing` 政策速报 · `alliance-promotion` 联盟推广

**开发商**：`progress-broadcast` 工程进展播报 · `referral-growth` 老带新裂变 · `crisis-response` 客诉危机应答

配置示例：

```yaml
skill:
  archetype: developer-sales      # 选角色原型
  modules:                        # 按需挂模块
    - ad-compliance
    - customer-followup
```

## 一份 brand.yaml = 一个品牌

模板保持行业通用，品牌差异全部在配置层：

```yaml
brand:   { name: 春城置业, cities: [昆明] }
skill:   { archetype: consumer-buy, modules: [estate-review, ad-compliance] }
adapter: { id: mock }              # 换真实数据源时换这里
content: { 城市板块知识、话术、触发词…… 40+ 可配槽位 }
```

## 安装到 Agent

```bash
bash install.sh output/kunming-buy              # 自动探测 ~/.hermes/skills 等
bash install.sh output/kunming-buy ~/my-agent/skills   # 手动指定
```

支持 Hermes(`HERMES_HOME`) / OpenClaw / Claude Code / Codex / 自定义目录；安装时校验 manifest 并记录 sha256。

## 数据适配器

mock 适配器零依赖演示接口契约（`adapters/mock/mock_cli.py`，search/detail/resblock 三个能力+虚构数据声明）。接真实数据源：复制 mock 目录实现同三个能力，`adapter.id` 一换、`adapter_usage` 一改，模板零改动。

## 给同行的商业用法

- 骨架开源获信任；每接一家客户 = 一份 brand.yaml + 一个数据适配器（1~2 天交付）；
- 深度 know-how（板块数据、话术库、佣金政策）全放配置层，由品牌方自持不必开源；
- 多角色组合销售：开发商买 developer-sales，中介买 brokerage-agent + consumer-buy，渠道公司买 channel-distributor。

## 目录结构

```
house-skills-kit/
├── template/
│   ├── archetypes/          # 四角色原型模板
│   │   ├── consumer-buy.md.tmpl
│   │   ├── developer-sales.md.tmpl
│   │   ├── brokerage-agent.md.tmpl
│   │   └── channel-distributor.md.tmpl
│   └── modules/             # 四个可挂载增值模块
├── brand.example.yaml       # 配置 schema 示例
├── render.py                # 渲染器(原型组装+模块挂载+占位符校验)
├── install.sh               # 安装器(manifest校验/多Agent探测/sha256)
├── adapters/mock/           # 零依赖演示适配器
└── examples/
    ├── kunming/             # C端买房示例(昆明板块know-how)
    └── developer/           # 开发商案场示例
```

## 质量承诺

每次发布的正文均通过自动比对（句级+15字滑窗）确认与参照项目无文本重合，框架层借鉴、表达层原创。

## 许可

Apache-2.0
