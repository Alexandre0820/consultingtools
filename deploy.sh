#!/bin/bash

# GitHub Pages 一键部署脚本
# 用法：./deploy.sh

set -e  # 遇到错误立即停止

echo "🚀 开始部署到 GitHub Pages..."
echo ""

# 1. 检查Git是否安装
if ! command -v git &> /dev/null; then
    echo "❌ Git未安装，请先安装Git：https://git-scm.com/downloads"
    exit 1
fi

# 2. 检查是否在正确目录
if [ ! -f "index.html" ]; then
    echo "❌ 请在项目根目录下运行此脚本"
    exit 1
fi

# 3. 初始化Git（如果未初始化）
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
fi

# 4. 添加文件
echo "➕ 添加文件到暂存区..."
git add .

# 5. 提交
echo "✅ 提交更改..."
git commit -m "🚀 更新部署 $(date '+%Y-%m-%d %H:%M:%S')" || echo "（无新更改）"

# 6. 检查远程仓库
REMOTE_EXISTS=$(git remote | grep -c origin || true)
if [ "$REMOTE_EXISTS" -eq 0 ]; then
    echo ""
    echo "⚠️  未检测到远程仓库"
    echo "请在GitHub创建仓库后，运行以下命令添加远程地址："
    echo ""
    echo "  git remote add origin https://github.com/你的用户名/仓库名.git"
    echo ""
    echo "然后再次运行："
    echo "  ./deploy.sh"
    exit 0
fi

# 7. 推送到远程
echo "📤 推送到 GitHub..."
git push origin main || git push origin master

echo ""
echo "✅ 部署完成！"
echo ""
echo "📌 下一步："
echo "1. 进入GitHub仓库 → Settings → Pages"
echo "2. Source 选择 main/master 分支"
echo "3. Folder 选择 /root"
echo "4. 保存后访问：https://你的用户名.github.io/仓库名/"
echo ""
echo "或者使用自定义域名（在Pages设置中配置）"
echo ""
