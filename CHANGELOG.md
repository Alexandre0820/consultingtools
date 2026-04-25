# 咨询工具推荐前端 - v1.1 更新日志

**日期**：2026-04-25

## 新增功能

### 1. 分类系统优化
- 新增「市场调研」分类（Atypica AI）
- 新增「独立咨询」分类（Polsia）
- 修正AI工具筛选问题（category字段统一）

### 2. 工具更新
- **移除**：Notion AI
- **新增**：
  - Atypica AI（市场调研）→ 带「点我获取折扣」按钮，直接邮件联系
  - Polsia（独立咨询）→ 帮助独立咨询顾问评估创业和定位
  - DrawThis (GitHub) → Thinkcell开源替代品

### 3. 联系信息
- 页脚添加邮箱：contact-growth@proton.me

### 4. 折扣功能
- Atypica AI卡片新增绿色「点我获取折扣」按钮
- 点击直接打开邮件客户端，收件人：contact-growth@proton.me
- 可通过邮件联系获取专属折扣

## 工具清单（v1.1）

| 工具 | 分类 | 特色 |
|------|------|------|
| Notion | 项目管理 | 一体化工作空间 |
| Atypica AI | 市场调研 | AI驱动 + 折扣按钮 |
| NotebookLM | AI工具 | Google AI研究助手 |
| Polsia | 独立咨询 | 独立咨询顾问商业智能 |
| DrawThis | 数据分析 | Thinkcell开源替代 |

## 技术实现

### Logo资源
- 所有工具均使用官方/真实logo
- Atypica AI、Polsia、DrawThis 使用定制SVG
- 存储在 `assets/logos/` 目录

### 筛选分类
- 全部工具 / AI工具 / 数据分析 / 项目管理 / 研究工具 / 市场调研 / 独立咨询

## 下一步计划

- [ ] 添加更多工具（待用户提供）
- [ ] 实现工具对比功能
- [ ] 添加用户评价/评分
- [ ] 优化移动端体验
- [ ] 添加搜索历史/热门搜索
