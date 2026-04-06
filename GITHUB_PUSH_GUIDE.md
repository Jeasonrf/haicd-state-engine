# GitHub 推送指南 - HAICD State Engine

## 📋 仓库信息

### 基本信息
- **仓库名称**: haicd-state-engine
- **分支**: main

## 🚀 推送方案

### 方案 A: 使用 SSH 密钥（推荐）

#### 步骤 1: 生成 SSH 密钥
```bash
# 生成新的 SSH 密钥
ssh-keygen -t ed25519 -C "your-email@example.com"

# 查看公钥
cat ~/.ssh/id_ed25519.pub
```

#### 步骤 2: 添加公钥到 GitHub
1. 访问 GitHub Settings → SSH and GPG keys
2. 点击 "New SSH key"
3. 粘贴公钥内容
4. 保存

#### 步骤 3: 测试 SSH 连接
```bash
ssh -T git@github.com
# 应该看到认证成功消息
```

#### 步骤 4: 推送代码
```bash
cd [haicd-state-engine目录]
git push origin main
```

### 方案 B: 使用 Personal Access Token

#### 步骤 1: 创建 Token
1. 访问 GitHub Settings → Developer settings → Personal access tokens
2. 生成新的 token，勾选 "repo" 权限
3. 复制 token

#### 步骤 2: 使用 Token 推送
```bash
cd [haicd-state-engine目录]

# 使用 Token 设置远程仓库
git remote set-url origin https://x-access-token:[YOUR_TOKEN]@github.com/[username]/haicd-state-engine.git

# 推送
git push origin main
```

## 📁 文件清单

### v2.1.0 核心更新
1. 输出控制层集成框架
2. 多领域应用扩展（9领域18场景）
3. 配置兼容性修复
4. 术语标准化更新
5. 完整文档体系

### 新增文件
- 输出控制层脚本和文档
- 配置管理工具
- 中英文对照文档
- 多领域案例文档

## 🔧 故障排除

### 常见问题
1. **认证失败**: 检查 SSH 密钥或 Token 配置
2. **权限不足**: 确认有仓库写入权限
3. **网络问题**: 检查网络连接

### 验证推送
1. 检查 GitHub 仓库页面
2. 验证提交记录
3. 确认文件正确显示

## ⚠️ 注意事项

### 安全提示
1. 不要提交包含个人信息的文件
2. 妥善保管 SSH 私钥和 GitHub Token
3. 定期更新认证凭证

### 技术提示
1. 保持 Git 配置清洁
2. 使用 .gitignore 排除敏感文件
3. 定期备份重要数据

## 📞 帮助资源

- GitHub 文档: https://docs.github.com
- SSH 密钥指南: https://docs.github.com/authentication/connecting-to-github-with-ssh
- Git 教程: https://git-scm.com/book

---

**版本**: v1.0  
**日期**: 2026-04-06  
**用途**: HAICD State Engine GitHub 推送参考指南