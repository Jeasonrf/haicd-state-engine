#!/bin/bash
# 安全的 GitHub 连接测试脚本

echo "🔍 GitHub 连接和安全测试"
echo "============================================================"

# 测试 1: 检查 SSH 密钥
echo ""
echo "1. 检查 SSH 密钥..."
if [ -f ~/.ssh/id_ed25519.pub ] || [ -f ~/.ssh/id_rsa.pub ]; then
    echo "✅ SSH 密钥存在"
    if [ -f ~/.ssh/id_ed25519.pub ]; then
        echo "   • ED25519 密钥: 已配置"
    fi
    if [ -f ~/.ssh/id_rsa.pub ]; then
        echo "   • RSA 密钥: 已配置"
    fi
else
    echo "❌ 未找到 SSH 密钥"
    echo "   运行: ssh-keygen -t ed25519 -C \"your-email@example.com\""
fi

# 测试 2: 测试 SSH 连接
echo ""
echo "2. 测试 SSH 连接到 GitHub..."
ssh_output=$(ssh -T git@github.com 2>&1)
if echo "$ssh_output" | grep -q "successfully authenticated"; then
    echo "✅ SSH 认证成功"
    echo "   用户: 已认证"
else
    echo "❌ SSH 认证失败"
    echo "   错误: 认证失败（请检查 SSH 密钥配置）"
fi

# 测试 3: 检查 Git 远程仓库
echo ""
echo "3. 检查 Git 远程仓库..."
cd ~/.openclaw/skills/haicd-state-engine 2>/dev/null
if [ $? -eq 0 ]; then
    remote_url=$(git config --get remote.origin.url)
    if [ -n "$remote_url" ]; then
        echo "✅ 远程仓库已配置"
        
        # 检查仓库格式（不显示具体用户名）
        if echo "$remote_url" | grep -q "github.com"; then
            echo "   ✅ GitHub 仓库"
        else
            echo "   ⚠️  非 GitHub 仓库"
        fi
    else
        echo "❌ 未配置远程仓库"
    fi
else
    echo "❌ 无法进入 HAICD 目录"
fi

# 测试 4: 检查网络连接
echo ""
echo "4. 测试 GitHub API 连接..."
api_response=$(curl -s -I https://api.github.com 2>/dev/null | head -1)
if echo "$api_response" | grep -q "200"; then
    echo "✅ GitHub API 可访问"
else
    echo "❌ GitHub API 不可访问"
    echo "   请检查网络连接"
fi

# 测试 5: 检查隐私安全
echo ""
echo "5. 隐私安全检查..."
cd ~/.openclaw/skills/haicd-state-engine 2>/dev/null
if [ $? -eq 0 ]; then
    # 检查是否包含敏感信息
    sensitive_files=$(find . -type f \( -name "*.py" -o -name "*.json" -o -name "*.yaml" -o -name "*.md" -o -name "*.sh" \) -exec grep -l "password\|secret\|key\|token\|api_key" {} \; 2>/dev/null | head -5)
    
    if [ -z "$sensitive_files" ]; then
        echo "✅ 未发现明显的敏感信息"
    else
        echo "⚠️  发现可能包含敏感信息的文件:"
        echo "$sensitive_files" | while read file; do
            echo "   • $(basename "$file")"
        done
        echo "   建议检查这些文件的内容"
    fi
else
    echo "❌ 无法进行隐私检查"
fi

echo ""
echo "============================================================"
echo "📋 测试总结:"

# 总结建议
if echo "$ssh_output" | grep -q "successfully authenticated" && \
   [ -n "$remote_url" ]; then
    echo "✅ 基本连接测试通过"
    echo ""
    echo "🚀 可以尝试推送:"
    echo "   cd ~/.openclaw/skills/haicd-state-engine"
    echo "   ./push_to_github_safe.sh"
else
    echo "⚠️  需要修复一些问题才能推送"
    echo ""
    echo "🔧 修复建议:"
    
    if ! echo "$ssh_output" | grep -q "successfully authenticated"; then
        echo "1. 设置 SSH 密钥:"
        echo "   ssh-keygen -t ed25519 -C \"your-email@example.com\""
        echo "   然后将公钥添加到 GitHub"
    fi
    
    if [ -z "$remote_url" ]; then
        echo "2. 设置远程仓库:"
        echo "   git remote add origin [你的仓库URL]"
    fi
    
    echo ""
    echo "📖 详细指南见: GITHUB_PUSH_GUIDE.md"
fi

echo ""
echo "🔗 有用的链接:"
echo "• SSH 密钥设置: https://docs.github.com/authentication/connecting-to-github-with-ssh"
echo "• GitHub 安全最佳实践: https://docs.github.com/authentication/keeping-your-account-and-data-secure"