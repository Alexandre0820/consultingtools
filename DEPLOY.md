# GitHub Pages 部署完整指南

## 前置准备

1. **GitHub账号**（没有请先注册）
2. **Git命令行工具**（macOS自带，验证：`git --version`）
3. **项目文件**：当前目录 `~/咨询顾问工具`

---

## 部署步骤

### 第一步：创建GitHub仓库

1. 登录 GitHub (https://github.com)
2. 点击右上角 `+` → `New repository`
3. 仓库信息：
   - **Repository name**: `growth-tools` (或你喜欢的名字)
   - **Description**: `Consulting tools recommendation platform`
   - **Public** (公开)
   - ✅ **Add a README file** (可选)
   - **Add .gitignore** → 选择 `Node`
4. 点击 `Create repository`

---

### 第二步：本地Git初始化

在终端中执行（我已经帮你定位到项目目录）：

```bash
# 1. 进入项目目录
cd /Users/shengyun/lobsterai/咨询顾问工具

# 2. 初始化Git
git init

# 3. 查看状态
git status

# 4. 添加所有文件
git add .

# 5. 提交
git commit -m "🎉 初始发布：咨询工具推荐平台 v1.0"
```

---

### 第三步：连接到远程仓库

在GitHub仓库页面，复制SSH或HTTPS URL：

```bash
# HTTPS方式（推荐新手）
git remote add origin https://github.com/你的用户名/growth-tools.git

# 或SSH方式（需要配置SSH key）
git remote add origin git@github.com:你的用户名/growth-tools.git
```

---

### 第四步：推送到GitHub

```bash
# 推送主分支
git push -u origin main

# 如果提示main不存在，使用：
git push -u origin master
```

---

### 第五步：启用GitHub Pages

1. 进入仓库 → **Settings**
2. 左侧菜单 → **Pages**
3. **Build and deployment**:
   - Source: `Deploy from a branch`
   - Branch: `main` (或 `master`)
   - Folder: `/root`
4. 点击 **Save**

等待1-2分钟，页面会显示：
```
Your site is live at https://你的用户名.github.io/growth-tools/
```

---

## 后续更新网站

修改 `index.html` 后，执行：

```bash
# 1. 查看改动
git status

# 2. 添加修改
git add .

# 3. 提交
git commit -m "更新：添加新工具Atypica AI"

# 4. 推送
git push
```

GitHub Pages会自动重新部署（约30秒-1分钟）。

---

## 自定义域名（可选）

1. 购买域名（如 `yourdomain.com`）
2. 在仓库 Settings → Pages → Custom domain
3. 输入域名，点击 Save
4. 在域名DNS设置中添加CNAME记录：
   ```
   CNAME 你的用户名.github.io
   ```
5. 等待生效（几分钟到几小时）

---

## 常见问题

### Q1: 推送失败提示权限错误
**A**: 使用HTTPS方式，Git会要求输入GitHub用户名和密码（或Personal Access Token）。

### Q2: 图片/资源加载失败
**A**: 确保所有资源路径是相对路径（如 `assets/logos/notion.png`），不要用绝对路径。

### Q3: 部署后样式丢失
**A**: 检查Tailwind CDN是否能访问（需要网络），或考虑下载Tailwind到本地。

### Q4: 如何回滚到之前的版本
**A**:
```bash
git log  # 查看提交历史
git revert <commit-hash>  # 回滚某个提交
git push
```

---

## 我可以帮你做的

✅ **已完成**：
- 所有代码文件已准备好
- 资源文件已整理好
- README.md已生成

⏳ **需要你手动操作**：
1. 创建GitHub仓库
2. 执行git命令推送
3. 在GitHub设置中启用Pages

需要我帮你执行git命令吗？如果你已经配置好了GitHub认证，我可以直接帮你完成推送。

---

**遇到问题随时问我！** 🚀
