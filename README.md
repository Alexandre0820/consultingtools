# 增长 Growth Croissance - 咨询工具推荐平台

为管理咨询和战略咨询顾问打造的专业工具推荐平台，精选AI、数据分析、项目管理等高效工具。

## 快速部署

本项目为纯静态HTML网站，可直接部署到任何静态托管平台：

### GitHub Pages 部署步骤

1. **创建GitHub仓库**
   ```bash
   # 在GitHub上创建新仓库，命名为：growth-tools
   # 建议设为Public（公开）
   ```

2. **本地初始化Git**
   ```bash
   cd /Users/shengyun/lobsterai/咨询顾问工具
   git init
   git add .
   git commit -m "初始提交：咨询工具推荐平台"
   ```

3. **推送到GitHub**
   ```bash
   git remote add origin https://github.com/你的用户名/growth-tools.git
   git branch -M main
   git push -u origin main
   ```

4. **启用GitHub Pages**
   - 进入仓库 Settings → Pages
   - Source 选择 "Deploy from a branch"
   - Branch 选择 `main` 分支，文件夹 `/root`
   - 保存后等待1-2分钟，即可访问 `https://你的用户名.github.io/growth-tools/`

## 项目结构

```
├── index.html              # 主页面
├── assets/
│   ├── logos/             # 工具图标
│   └── qrcode/            # 公众号二维码
└── README.md              # 本文件
```

## 技术栈

- **HTML5 + Tailwind CSS**（CDN加载）
- **原生JavaScript**（无框架依赖）
- **响应式设计**（移动端友好）

## 后续维护

如需添加/修改工具，直接编辑 `index.html` 中的 `toolsData` 数组即可。

---

**Made with ❤️ by 增长 Growth Croissance**
