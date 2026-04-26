# 咨询工具推荐前端 - v1.4 更新日志

**日期**：2026-04-26

## 内容本地化完善

### 工具卡片内容双语化
所有工具的中文描述、推荐理由、适用场景均已翻译为英文，并在切换语言时自动显示对应版本：

| 工具字段 | 中文字段 | 英文字段 |
|---------|---------|---------|
| 描述 | `description` | `description_en` |
| 推荐理由 | `recommendation` | `recommendation_en` |
| 适用场景 | `useCases[]` | `useCases_en[]` |

### 支持完整双语的工具（7个）
1. **Notion** - 项目管理
2. **Atypica AI** - 市场调研（含折扣链接）
3. **Xavier AI** - AI工具（含联系我们按钮）
4. **NotebookLM** - AI研究助手
5. **Typeless** - 语音输入键盘（含折扣码）
6. **Polsia** - 独立咨询商业智能（含折扣链接）
7. **DrawThis** - 开源图表工具

### 渲染逻辑
- 语言切换时，`renderTools()` 自动根据 `currentLang` 选择中/英文字段
- UI界面元素（按钮、标签等）通过 `data-i18n` 和 `translations` 对象动态更新
- 英文模式下显示 `description_en`、`recommendation_en`、`useCases_en`
- 中文模式下显示原有字段

---

**v1.4 实现了工具内容的完整国际化，用户体验更加流畅**
