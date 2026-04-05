#!/bin/bash
# HAICD 输出控制层启用脚本

echo "🔧 启用 HAICD 输出控制层..."

# 检查 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

# 运行设置脚本
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

if python3 haicd_output_control_setup.py --enable; then
    echo "✅ HAICD 输出控制层启用成功"
    echo ""
    echo "📋 启用状态："
    echo "• 输出控制层: 已启用"
    echo "• 状态跟踪: 已启用"
    echo "• 意义评估: 已启用"
    echo ""
    echo "📊 监控命令:"
    echo "  ./control/status_haicd.sh"
    echo ""
    echo "🔄 禁用命令:"
    echo "  ./control/disable_haicd.sh"
else
    echo "❌ HAICD 输出控制层启用失败"
    exit 1
fi