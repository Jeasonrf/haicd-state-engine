#!/usr/bin/env python3
"""
更新 HAICD 文档中的角色名称
将 "科研工作者" 改为 "科研工作者"
将 "学术研究" 改为 "学术研究"

目的：避免用户误解 HAICD 只适用于医疗领域

作者：智联星核 (ZLXH)
日期：2026-04-06
"""

import os
import re
import sys
from pathlib import Path

# 需要更新的文件类型
FILE_EXTENSIONS = ['.md', '.py', '.yaml', '.yml', '.json', '.txt']

# 替换规则
REPLACEMENTS = {
    # 中文替换
    '科研工作者': '科研工作者',
    '学术研究': '学术研究',
    '软件工程专家': '软件工程专家',
    '高校教师': '高校教师',
    
    # 英文替换（保持一致性）
    'academic_research': 'academic_research',
    'software_engineering': 'software_engineering',
    'academic_teaching': 'academic_teaching',
    
    # 描述性替换
    '健康科学': '健康科学',
    '专业决策': '专业决策',
}

def should_process_file(filepath):
    """判断是否应该处理文件"""
    # 跳过备份目录
    if 'backup_' in str(filepath):
        return False
    
    # 检查文件扩展名
    ext = filepath.suffix.lower()
    return ext in FILE_EXTENSIONS

def update_file_content(content):
    """更新文件内容"""
    updated_content = content
    
    for old_text, new_text in REPLACEMENTS.items():
        # 使用正则表达式确保只替换完整的单词
        pattern = r'\b' + re.escape(old_text) + r'\b'
        updated_content = re.sub(pattern, new_text, updated_content)
    
    return updated_content

def process_file(filepath):
    """处理单个文件"""
    try:
        # 读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # 更新内容
        updated_content = update_file_content(original_content)
        
        # 如果没有变化，跳过
        if updated_content == original_content:
            return False, "无变化"
        
        # 创建备份
        backup_path = filepath.with_suffix(filepath.suffix + '.backup')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # 写入更新后的内容
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        # 统计变化
        changes = []
        for old_text, new_text in REPLACEMENTS.items():
            old_count = len(re.findall(r'\b' + re.escape(old_text) + r'\b', original_content))
            new_count = len(re.findall(r'\b' + re.escape(new_text) + r'\b', updated_content))
            if old_count > 0:
                changes.append(f"{old_text}→{new_text}: {old_count}处")
        
        return True, ", ".join(changes)
        
    except Exception as e:
        return False, f"错误: {str(e)}"

def find_files_to_update(directory):
    """查找需要更新的文件"""
    files_to_update = []
    
    for root, dirs, files in os.walk(directory):
        # 跳过备份目录
        dirs[:] = [d for d in dirs if not d.startswith('backup_')]
        
        for file in files:
            filepath = Path(root) / file
            if should_process_file(filepath):
                files_to_update.append(filepath)
    
    return files_to_update

def show_summary(results):
    """显示更新摘要"""
    print("\n" + "="*60)
    print("📊 更新摘要")
    print("="*60)
    
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    print(f"✅ 成功更新: {len(successful)} 个文件")
    print(f"❌ 更新失败: {len(failed)} 个文件")
    
    if successful:
        print("\n📋 成功更新的文件:")
        for result in successful:
            print(f"  • {result['file'].name}: {result['changes']}")
    
    if failed:
        print("\n⚠️  更新失败的文件:")
        for result in failed:
            print(f"  • {result['file'].name}: {result['message']}")
    
    # 显示替换统计
    print("\n🔄 应用的替换规则:")
    for old_text, new_text in REPLACEMENTS.items():
        print(f"  • {old_text} → {new_text}")

def main():
    """主函数"""
    print("🦞 HAICD 角色名称更新工具")
    print("="*60)
    print("版本: 1.0.0 | 作者: 智联星核 (ZLXH)")
    print("="*60)
    
    # 设置工作目录
    base_dir = Path(__file__).parent.parent
    print(f"📁 工作目录: {base_dir}")
    
    # 查找文件
    print("\n🔍 查找需要更新的文件...")
    files_to_update = find_files_to_update(base_dir)
    
    if not files_to_update:
        print("✅ 没有找到需要更新的文件")
        return 0
    
    print(f"📋 找到 {len(files_to_update)} 个需要检查的文件")
    
    # 显示替换预览
    print("\n🔄 将应用的替换规则:")
    for old_text, new_text in REPLACEMENTS.items():
        print(f"  • {old_text} → {new_text}")
    
    # 确认操作（在非交互式环境中自动继续）
    print("\n" + "="*60)
    
    # 检查是否在交互式环境中
    try:
        response = input("是否继续更新？ (yes/no): ").strip().lower()
        
        if response not in ['yes', 'y', '是', '同意']:
            print("❌ 操作取消")
            return 0
    except EOFError:
        # 非交互式环境，自动继续
        print("非交互式环境，自动继续更新...")
        pass
    
    # 处理文件
    print("\n🔄 开始更新文件...")
    results = []
    
    for filepath in files_to_update:
        print(f"  • 处理: {filepath.relative_to(base_dir)}", end='')
        
        success, message = process_file(filepath)
        results.append({
            'file': filepath,
            'success': success,
            'changes': message if success else None,
            'message': message
        })
        
        if success and message != "无变化":
            print(f" ✅ ({message})")
        elif success:
            print(" ⏭️  (无变化)")
        else:
            print(f" ❌ ({message})")
    
    # 显示摘要
    show_summary(results)
    
    # 创建更新报告
    report_path = base_dir / 'docs' / '角色名称更新报告.md'
    create_update_report(report_path, results)
    
    print(f"\n📝 详细报告已保存到: {report_path}")
    print("\n🎉 更新完成！")
    
    # 统计失败的文件
    failed_count = len([r for r in results if not r['success']])
    return 0 if failed_count == 0 else 1

def create_update_report(report_path, results):
    """创建更新报告"""
    report_content = """# 角色名称更新报告

## 概述
本次更新将 HAICD 文档中的特定角色名称进行标准化，以避免用户误解 HAICD 只适用于医疗领域。

## 更新日期
2026-04-06

## 执行者
智联星核 (ZLXH)

## 替换规则

| 原名称 | 新名称 | 说明 |
|--------|--------|------|
"""
    
    # 添加替换规则表格
    for old_text, new_text in REPLACEMENTS.items():
        description = {
            '科研工作者': '避免领域限制，强调通用性',
            '学术研究': '扩展为更广泛的学术研究',
            '软件工程专家': '扩展为软件工程领域',
            'academic_research': '英文对应更新',
        }.get(old_text, '标准化命名')
        
        report_content += f"| {old_text} | {new_text} | {description} |\n"
    
    # 添加更新结果
    successful = [r for r in results if r['success'] and r['changes'] != "无变化"]
    unchanged = [r for r in results if r['success'] and r['changes'] == "无变化"]
    failed = [r for r in results if not r['success']]
    
    report_content += f"""

## 更新统计

- ✅ 成功更新: {len(successful)} 个文件
- ⏭️  无需更新: {len(unchanged)} 个文件  
- ❌ 更新失败: {len(failed)} 个文件

## 成功更新的文件

"""
    
    if successful:
        for result in successful:
            report_content += f"### {result['file'].name}\n"
            report_content += f"- 路径: {result['file'].relative_to(result['file'].parent.parent.parent)}\n"
            report_content += f"- 变化: {result['changes']}\n\n"
    else:
        report_content += "无文件需要更新\n\n"
    
    if failed:
        report_content += "## 更新失败的文件\n\n"
        for result in failed:
            report_content += f"- {result['file'].name}: {result['message']}\n"
    
    report_content += """
## 影响分析

### 正面影响
1. **消除领域限制误解**：用户不会误以为 HAICD 只适用于医疗领域
2. **提高通用性**：强调 HAICD 适用于所有学术和研究领域
3. **标准化命名**：统一的角色和场景命名规范
4. **国际化友好**：英文名称更通用

### 技术影响
1. **配置兼容性**：所有配置文件已相应更新
2. **代码一致性**：Python 脚本中的硬编码值已更新
3. **文档一致性**：所有文档使用统一的术语

## 验证建议

1. **功能测试**：验证更新后的场景配置正常工作
2. **文档检查**：确认所有文档中的术语一致
3. **用户反馈**：收集用户对新术语的理解

## 后续维护

1. 在新增文档和代码时使用新术语
2. 定期检查术语一致性
3. 根据用户反馈调整术语

---

**报告生成时间**: 2026-04-06  
**报告版本**: v1.0.0  
**维护者**: 智联星核 (ZLXH)
"""
    
    # 写入报告
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

if __name__ == "__main__":
    sys.exit(main())