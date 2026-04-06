#!/bin/bash
# 安全推送脚本 - 不包含隐私信息

echo "🚀 HAICD State Engine GitHub 安全推送"
echo "============================================================"

# 检查当前目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ ! -f "SKILL.md" ]; then
    echo "❌ 错误: 请在 HAICD 技能目录运行此脚本"
    exit 1
fi

echo "📋 当前目录: $(pwd)"
echo ""

# 检查 Git 状态
if ! git status &> /dev/null; then
    echo "❌ 错误: 不是 Git 仓库"
    exit 1
fi

# 显示基本信息
echo "🔍 仓库信息:"
echo "• 分支: $(git branch --show-current)"
REMOTE_URL=$(git config --get remote.origin.url)
echo "• 远程仓库: ${REMOTE_URL:-未设置}"

echo ""
echo "📊 本地提交状态:"
LOCAL_COMMITS=$(git log --oneline origin/main..HEAD 2>/dev/null | wc -l)
if [ "$LOCAL_COMMITS" -gt 0 ]; then
    echo "✅ 有 $LOCAL_COMMITS 个本地提交待推送"
    git log --oneline -3 origin/main..HEAD 2>/dev/null || git log --oneline -3
else
    echo "⚠️  没有待推送的本地提交"
fi

echo ""
echo "🔄 准备推送..."

# 安全提示
echo ""
echo "⚠️  安全提示:"
echo "1. 确保不包含隐私信息（API密钥、密码等）"
echo "2. 确认远程仓库 URL 正确"
echo "3. 检查 .gitignore 文件排除敏感文件"
echo ""

# 确认推送
read -p "是否继续推送？ (输入 'yes' 继续): " confirm

if [[ "$confirm" != "yes" ]]; then
    echo "❌ 操作取消"
    exit 0
fi

echo ""
echo "🚀 开始推送..."

# 尝试推送
if git push origin main; then
    echo ""
    echo "🎉 推送成功！"
    echo ""
    echo "📊 推送详情:"
    echo "• 时间: $(date)"
    echo "• 最新提交: $(git log --oneline -1 --format='%h - %s')"
    echo ""
    echo "🔗 建议验证:"
    echo "1. 访问 GitHub 仓库页面"
    echo "2. 检查提交记录"
    echo "3. 确认文件正确显示"
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "🔧 可能的原因:"
    echo "1. 认证失败（SSH 密钥或 Token）"
    echo "2. 网络连接问题"
    echo "3. 权限不足"
    echo ""
    echo "🛠️  解决方案:"
    echo "1. 检查 Git 远程配置: git remote -v"
    echo "2. 测试连接: ssh -T git@github.com (SSH)"
    echo "3. 查看详细错误信息"
    echo ""
    echo "📖 参考指南: GITHUB_PUSH_GUIDE.md"
    exit 1
fi

echo ""
echo "============================================================"
echo "✅ 推送流程完成"
echo ""
echo "💡 后续建议:"
echo "1. 定期更新代码"
echo "2. 使用分支进行开发"
echo "3. 保持提交信息清晰"
echo "4. 定期检查安全设置"