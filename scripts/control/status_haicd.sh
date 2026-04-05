#!/bin/bash
# HAICD 输出控制层状态检查脚本

echo "📊 HAICD 输出控制层状态检查..."

# 检查 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

# 运行设置脚本
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

python3 haicd_output_control_setup.py --status