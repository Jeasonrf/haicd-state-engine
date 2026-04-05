#!/bin/bash
# HAICD 输出控制层禁用脚本

echo "🔧 禁用 HAICD 输出控制层..."

# 检查 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

# 运行设置脚本
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

if python3 haicd_output_control_setup.py --disable; then
    echo "✅ HAICD 输出控制层禁用成功"
    echo ""
    echo "📋 禁用状态："
    echo "• 输出控制层: 已禁用"
    echo "• 状态跟踪: 已停止"
    echo "• 意义评估: 已停止"
    echo ""
    echo "🔄 重新启用命令:"
    echo "  ./control/enable_haicd.sh"
else
    echo "❌ HAICD 输出控制层禁用失败"
    exit 1
fi