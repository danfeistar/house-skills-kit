# 发布指南：GitHub + 国内镜像 + 个人品牌

## 一、GitHub 主站发布（10 分钟）

### 1. 建仓（网页操作）
- 登录 GitHub → New repository → 名称 `house-skills-kit` → Public → **不要**勾选自动生成 README/LICENSE（本地已齐）
- 描述填：`中文房产 AI 技能生成骨架 · 企业与个人从业者通用 · 4类角色 × 29个业务模块 · 一份配置生成品牌专属Skill · Apache-2.0`

### 2. 推送（本地执行）
```bash
cd /opt/data/house-skills-kit
git remote add origin git@github.com:<你的用户名>/house-skills-kit.git
git push -u origin master
```
> 建议同时建 tag：`git tag v0.5.0 && git push --tags`（Releases 页挂 zip，方便非开发者下载）

### 3. About 栏 topics（重要，决定被搜到）
`real-estate` `claude-skills` `agent-skills` `ai-agent` `proptech` `chinese` `prompt-engineering` `real-estate-agent` `house` `skill-template`

## 二、国内镜像/同类平台（让国内企业搜得到）

| 平台 | 怎么发 | 优先级 |
|---|---|---|
| **Gitee（码云）** | 新建仓库 → 选"导入已有仓库"→ 填 GitHub 地址，之后每次 push 手动同步一次 | ★★★ 必发，国内企业默认搜这里 |
| **AtomGit** | 目前的替代方案：直接 MEDIA 发 zip 包给对方（用户习惯已验证） | ★★ 备用 |
| **GitCode（CSDN系）** | 用 CSDN 账号一键导入 GitHub 仓库 | ★★ 有 CSDN 账号就顺手开 |
| **OpenCSG / 魔乐社区** | 模型/工具类开源社区，可发工具包 | ★ 可后置 |

> 镜像同步成本极低：Gitee 导入一次后，点一下"同步"按钮即可。**GitHub 为主库，国内只做镜像**，issue 统一回 GitHub 处理。

## 三、让目标用户找到你（打标签+导流）

### 1. README 顶部身份卡（已写入 README）
```
作者：老何 ｜ 地产行业 10+ 年，深耕昆明
正在做：昆明房产 AI 工具平台（经纪人端+买房者端）
专注：把 AI 真正装进中国地产企业的日常工作流
联系：<微信/邮箱占位，发布前填>
```
>原则：**身份卡讲"谁在维护、为什么他懂行"**，这是国际项目给不了的信任状——海外 skills 仓库 90% 是工程师写的，地产行业老兵亲自写业务 SOP 的仓库几乎没有，这就是你的标签。

### 2. 提交到技能目录（免费精准流量）
- **awesome-claude-skills**（14.8k★）：提 PR 加一行到行业分类，PR 模板照抄仓库 CONTRIBUTING
- **awesome-skills-zh**（中文精选列表）：提 PR 到"垂直领域"分类，标注"中文房产垂类首个"
- **agentskill.sh / awesomeskill.ai**：自动抓取 GitHub，无需提交，push 后 1-2 天自动收录
- Anthropic 官方 skills 生态页如果开放投稿再跟

### 3. 内容导流（发布周做一轮）
- 小红书/抖音（你已有账号）：一条"我把10年地产经验做成了开源AI技能包"——讲判客/佣金政策/案场话术三个模块怎么来的，评论区放 GitHub 链接
- 知乎：回答"房产中介怎么用AI"类问题，正文挂仓库
- 微信朋友圈：配 release 截图 + 一句话

### 4. SEO 关键词布局（已埋进 README）
`房产中介 AI` `案场 AI` `分销渠道管理 AI` `判客` `佣金政策` `SKILL.md 房产` —— 企业用户搜这些词时 README 能命中。

## 四、发布后维护节奏
- issue 24h 内响应（初期 star 少，响应率=口碑）
- 每接一个真实客户，脱敏后加一个 `examples/` 案例（最有说服力的营销）
- 版本节奏：小版本按模块加，大版本按原型加
