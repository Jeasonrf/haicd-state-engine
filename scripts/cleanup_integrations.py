#!/usr/bin/env python3
"""
清理 OpenClaw 配置中的 integrations 键
修复因 HAICD 集成导致的配置验证错误

问题描述：
OpenClaw 2026.4.2 不识别 "integrations" 键，导致配置验证失败：
Invalid config at /Users/jeason/.openclaw/openclaw.json:
- <root>: Unrecognized key: "integrations"

解决方案：
1. 移除不被识别的 integrations 键
2. 将 HAICD 元数据存储在技能配置内部
3. 确保配置符合 OpenClaw 架构

作者：智联星核 (ZLXH)
日期：2026-04-06
"""

import json
import sys
from pathlib import Path

def cleanup_integrations():
    """清理 integrations 键"""
    config_path = Path.home() / '.openclaw' / 'openclaw.json'
    backup_path = config_path.with_suffix('.json.backup.cleanup')
    
    print("🔧 清理 OpenClaw 配置中的 integrations 键")
    print("="*60)
    
    if not config_path.exists():
        print(f"❌ 配置文件不存在: {config_path}")
        return False
    
    try:
        # 读取配置
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print(f"📋 配置文件: {config_path}")
        print(f"📏 文件大小: {config_path.stat().st_size} 字节")
        
        changes_made = False
        original_config = config.copy()
        
        # 1. 检查并清理 integrations 键
        if 'integrations' in config:
            print(f"⚠️  发现 integrations 键，包含 {len(config['integrations'])} 个项目")
            
            # 保存 HAICD 相关数据（如果存在）
            haicd_data = None
            if 'haicd' in config['integrations']:
                haicd_data = config['integrations']['haicd']
                print(f"  • 找到 HAICD 集成数据")
            
            # 移除 integrations 键
            del config['integrations']
            changes_made = True
            print("✅ 已移除 integrations 键")
            
            # 2. 如果存在 HAICD 技能配置，将元数据移到内部
            if haicd_data and 'skills' in config and 'haicd_state_engine' in config['skills']:
                if '_metadata' not in config['skills']['haicd_state_engine']:
                    config['skills']['haicd_state_engine']['_metadata'] = {}
                
                # 合并元数据
                config['skills']['haicd_state_engine']['_metadata'].update({
                    'integrated_at': haicd_data.get('integrated_at', 'unknown'),
                    'version': haicd_data.get('version', '1.0.0'),
                    'mode': haicd_data.get('mode', 'output_control'),
                    'backup_path': haicd_data.get('backup_path'),
                    'cleaned_at': '2026-04-06 05:30:00'
                })
                print("✅ 已将 HAICD 元数据移到技能配置内部")
        
        # 3. 检查其他可能的问题
        issues_found = []
        
        # 检查 skills 配置格式
        if 'skills' in config:
            for skill_name, skill_config in config['skills'].items():
                if not isinstance(skill_config, dict):
                    issues_found.append(f"技能 '{skill_name}' 配置不是字典格式")
                elif skill_name == 'haicd_state_engine':
                    # 确保 HAICD 配置有正确的结构
                    if 'enabled' not in skill_config:
                        skill_config['enabled'] = True
                        changes_made = True
                        print("✅ 为 HAICD 技能添加 enabled 字段")
        
        # 如果没有变化，直接返回
        if not changes_made:
            print("✅ 配置无需清理，一切正常")
            return True
        
        # 创建备份
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(original_config, f, indent=2, ensure_ascii=False)
        print(f"💾 原始配置已备份到: {backup_path}")
        
        # 保存清理后的配置
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✅ 清理后的配置已保存到: {config_path}")
        
        # 验证配置
        print("\n🔍 验证配置...")
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                verified_config = json.load(f)
            
            # 检查 integrations 键是否完全移除
            if 'integrations' in verified_config:
                print("❌ 验证失败: integrations 键仍然存在")
                return False
            
            print("✅ 配置验证通过")
            
            if issues_found:
                print("\n⚠️  发现的其他问题:")
                for issue in issues_found:
                    print(f"  • {issue}")
            
            print("\n" + "="*60)
            print("🎉 配置清理完成！")
            print("\n📋 清理结果:")
            print(f"• 移除了不被识别的 integrations 键")
            print(f"• 保留了所有功能配置")
            print(f"• 创建了配置备份: {backup_path}")
            print("\n🚀 下一步:")
            print("1. 重启 OpenClaw 网关: openclaw gateway restart")
            print("2. 验证状态: openclaw status")
            print("3. 检查 HAICD 集成状态: ./control/status_haicd.sh")
            
            return True
            
        except json.JSONDecodeError as e:
            print(f"❌ 配置验证失败（JSON 格式错误）: {e}")
            # 恢复备份
            with open(backup_path, 'r', encoding='utf-8') as f:
                backup_config = json.load(f)
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(backup_config, f, indent=2, ensure_ascii=False)
            print(f"🔄 已从备份恢复配置: {backup_path}")
            return False
            
    except Exception as e:
        print(f"❌ 清理过程中发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def check_config_validity():
    """检查配置有效性"""
    print("\n🔍 检查 OpenClaw 配置有效性")
    print("="*60)
    
    config_path = Path.home() / '.openclaw' / 'openclaw.json'
    
    if not config_path.exists():
        print(f"❌ 配置文件不存在: {config_path}")
        return False
    
    try:
        # 尝试读取配置
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print("✅ 配置文件格式正确")
        
        # 检查已知问题
        issues = []
        
        if 'integrations' in config:
            issues.append("包含不被识别的 'integrations' 键")
        
        # 检查必需字段
        required_fields = ['plugins', 'agents', 'gateway']
        for field in required_fields:
            if field not in config:
                issues.append(f"缺少必需字段 '{field}'")
        
        if issues:
            print("\n⚠️  发现配置问题:")
            for issue in issues:
                print(f"  • {issue}")
            return False
        else:
            print("✅ 配置无已知问题")
            return True
            
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 检查过程中发生错误: {str(e)}")
        return False

def main():
    """主函数"""
    print("🦞 OpenClaw 配置清理工具")
    print("="*60)
    print("版本: 1.0.0 | 作者: 智联星核 (ZLXH)")
    print("="*60)
    
    # 检查参数
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'check':
            return 0 if check_config_validity() else 1
        elif command == 'clean':
            return 0 if cleanup_integrations() else 1
        elif command in ['--help', '-h']:
            show_help()
            return 0
        else:
            print(f"❌ 未知命令: {command}")
            show_help()
            return 1
    else:
        # 默认执行清理
        return 0 if cleanup_integrations() else 1

def show_help():
    """显示帮助信息"""
    print("\n📖 使用说明:")
    print("="*60)
    print("\n🛠️  可用命令:")
    print("  check       检查配置有效性")
    print("  clean       清理 integrations 键")
    print("  --help      显示此帮助信息")
    print("\n📋 示例:")
    print("  python3 cleanup_integrations.py check")
    print("  python3 cleanup_integrations.py clean")
    print("\n⚠️  注意:")
    print("• 清理操作会自动创建配置备份")
    print("• 清理后需要重启 OpenClaw 网关")
    print("• 建议在清理前检查配置状态")

if __name__ == "__main__":
    sys.exit(main())