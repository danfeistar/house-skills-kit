---
name: house-skills-kit
description: 中文房产AI顾问技能生成骨架。4类角色（购房客户/开发商案场/中介经纪人/渠道分销）× 29个业务模块，一份 brand.yaml 配置即可渲染出品牌专属的中文房产顾问 Skill。Use when a Chinese real-estate business (developer, brokerage, channel distributor, or home buyer platform) needs a brand-customized AI advisor skill.
license: Apache-2.0
---

# house-skills-kit

任何房开商、中介机构、渠道公司、个人房产从业者，都能用一份配置生成自己品牌的中文房产 AI 顾问技能。

## 快速开始（3 步）

1. 克隆本仓库（GitHub / Gitee 镜像均可）；
2. 复制 `examples/kunming/kunming.buy.yaml` 为你的 `brand.yaml`，修改品牌名、业务参数、启用的模块（`modules:` 列表即挂即用）；
3. 渲染：`python3 render.py --config brand.yaml --out output/my-brand/`，产出的 Markdown 即为可直接投喂大模型的顾问技能正文。

## 角色原型 × 模块（29 个）

| 原型 | 适用 | 推荐模块 |
|---|---|---|
| consumer-buy | C端购房客户 | 楼盘评测、广告合规、贷款计算、资格问答 |
| developer-sales | 房开商案场 | 案场SOP、工程播报、老带新、危机应答 |
| brokerage-agent | 中介/个人经纪人 | 房源管理、客户管理、意向匹配、实勘、议价 |
| channel-distributor | 渠道分销公司 | 分销管理、内部判客、佣金政策、业绩监控 |

全部模块清单见 README；模块为挂载式，按需增删不影响骨架。

## 设计原则

- **顾问式 SOP + 意图路由**：先诊断需求再推荐，拒绝硬推；
- **合规红线内置**：虚假宣传零容忍、不承诺投资回报、风险如实揭示；
- **品牌数据与技能解耦**：所有业务参数走 brand.yaml / 适配器，接一家客户 = 一份配置；
- 正文 100% 原创撰写，方法论骨架参照社区公开的 Skill 分发最佳实践。

## 链接

- GitHub: https://github.com/danfeistar/house-skills-kit
- Gitee: https://gitee.com/danfeistar/house-skills-kit
- 作者：老何 — 地产从业 15+ 年，历任多家房企云南营销负责人
