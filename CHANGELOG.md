# 咨询工具推荐前端 - v1.6 更新日志

**日期**：2026-04-26

## 新增功能

### 企业级 AI 工具专区
- **位置**：工具展示区之后、关于我们之前
- **内容**：
  1. **素问 AI** - 医疗健康和生命科学领域的垂直大模型
     - 医学文献智能分析
     - 临床试验数据解读
     - 医疗知识问答系统
     - 药物研发智能辅助
  2. **企业 AI 平台**（预留）- 一体化企业级AI中台
  3. **智能 CRM 系统**（预留）- AI增强的客户关系管理

### 企业 AI 咨询与培训服务 CTA
- **位置**：页面中部显眼位置（深蓝色渐变背景）
- **设计**：全宽渐变背景 + 毛玻璃效果卡片 + 突出CTA按钮
- **三大核心服务**：
  1. **AI 转型陪跑** - 全程陪伴企业完成AI转型与流程变革
  2. **定义人机边界** - 科学规划AI与人类协作模式
  3. **员工技能提升** - 系统性培训企业AI人才梯队
- **行动号召**：
  - "立即咨询"按钮 → 邮件联系
  - "了解更多"按钮 → 返回工具区

## 国际化完善

### 新增翻译键（en）
- `enterprise_title` / `enterprise_subtitle`
- `suwen_ai` / `suwen_desc` / `suwen_recommend`
- `suwen_case1-4`（素问AI四个用例）
- `enterprise_platform` / `platform_desc` / `platform_recommend`
- `cta_title` / `cta_subtitle`
- `service1-3_title` / `service1-3_desc`
- `cta_contact` / `cta_learnmore`
- `contact_info` / `response_time`

### 技术实现
- 所有新添加的文本元素均使用 `data-i18n` 属性
- 复用现有 `setLanguage()` 自动切换机制
- 中英文双语支持完整

---

**v1.6 实现了企业级服务展示，增强了面向 To B 客户的价值传递**
