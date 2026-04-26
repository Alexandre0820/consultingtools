# 咨询工具推荐前端 - v1.3 更新日志

**日期**：2026-04-26

## 新增功能

### 中英文语言切换
- **位置**：右上角导航栏
- **功能**：支持中文/English一键切换
- **持久化**：自动保存用户语言偏好到localStorage
- **翻译范围**：
  - 导航菜单、按钮文本、筛选标签
  - 搜索placeholder
  - 页面标题和副标题
  - 工具卡片按钮（访问官网、获取折扣、联系我们）
  - 关于我们区域、页脚信息

## 工具更新

### 新增工具
- **Xavier AI**（AI工具类）→ 联系我们按钮直接邮件
- **Typeless**（AI工具类）→ 语音输入键盘+折扣码

### 功能优化
- **Atypica AI**：折扣链接改为直接跳转注册页 (`https://atypica.ai/?via=alex`)
- **Polsia**：添加折扣链接 (`https://polsia.com/?ref=KHL2FA7A`)

## 工具清单（v1.3）

| 工具 | 分类 | 特色 |
|------|------|------|
| Notion | 项目管理 | 一体化工作空间 |
| Atypica AI | 市场调研 | AI驱动 + 折扣链接 |
| Xavier AI | AI工具 | 智能助手 + 联系我们按钮 |
| NotebookLM | AI工具 | Google AI研究助手 |
| Typeless | AI工具 | 语音输入 + 折扣码 |
| Polsia | 独立咨询 | 独立咨询商业智能 + 折扣 |
| DrawThis | 数据分析 | Thinkcell开源替代 |

## 技术实现

### 国际化（i18n）架构
- 语言数据：`translations` 对象（zh/en）
- 切换函数：`setLanguage(lang)`
- 存储：localStorage (`preferred-lang`)
- 自动重绘：切换语言时刷新工具卡片
- 属性标记：`data-i18n` 标识需翻译元素

### 按钮系统
1. 访问官网（蓝色，所有工具）
2. 获取折扣（绿色边框，discountUrl字段）
3. 联系我们（蓝色边框，contactEmail字段）

### Logo资源
- 新增2个SVG logo（Xavier AI、Typeless）
- 总计8个工具图标（PNG + SVG混合）

---

**v1.3 实现了完整的国际化基础架构，后续可轻松扩展其他语言（如日语、韩语等）**
