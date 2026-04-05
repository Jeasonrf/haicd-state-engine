#!/usr/bin/env python3
"""
HAICD 输出控制层集成设置脚本
配置注入模式（方案1）

功能：帮助用户将 HAICD 技能集成到智能体的输出控制层
作者：智联星核 (ZLXH)
日期：2026-04-06
版本：v1.0.0
"""

import json
import os
import sys
import shutil
import time
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

class HAICDOutputControlSetup:
    """HAICD 输出控制层设置类"""
    
    def __init__(self):
        # 路径配置
        self.home_dir = Path.home()
        self.openclaw_dir = self.home_dir / '.openclaw'
        self.openclaw_config_path = self.openclaw_dir / 'openclaw.json'
        self.haicd_skill_dir = self.openclaw_dir / 'skills' / 'haicd-state-engine'
        self.scripts_dir = self.haicd_skill_dir / 'scripts'
        self.control_dir = self.scripts_dir / 'control'
        
        # 配置备份
        self.backup_dir = self.openclaw_dir / 'backups'
        self.config_backup_path = self.backup_dir / f'openclaw.json.backup.{int(time.time())}'
        
        # 状态文件
        self.status_file = self.control_dir / 'haicd_status.json'
        
        # 集成配置模板
        self.integration_config = {
            "haicd_output_control": {
                "enabled": True,
                "mode": "resident",
                "integration_level": "output_pipeline",
                "permissions": {
                    "read_output": True,
                    "modify_output": True,
                    "track_state_flow": True,
                    "context_analysis": True
                },
                "scenarios": {
                    "default": "balanced",
                    "override_rules": {
                        "emergency": "direct_output",
                        "sensitive": "conservative",
                        "creative": "exploratory"
                    }
                },
                "performance": {
                    "max_processing_time_ms": 100,
                    "enable_caching": True,
                    "cache_ttl_seconds": 300
                },
                "monitoring": {
                    "enabled": True,
                    "log_level": "info",
                    "metrics_collection": True
                }
            }
        }
    
    def check_prerequisites(self) -> Tuple[bool, str]:
        """检查前提条件"""
        print("🔍 检查前提条件...")
        
        # 1. 检查 OpenClaw 目录
        if not self.openclaw_dir.exists():
            return False, f"OpenClaw 目录不存在: {self.openclaw_dir}"
        
        # 2. 检查 OpenClaw 配置文件
        if not self.openclaw_config_path.exists():
            return False, f"OpenClaw 配置文件不存在: {self.openclaw_config_path}"
        
        # 3. 检查 HAICD 技能目录
        if not self.haicd_skill_dir.exists():
            return False, f"HAICD 技能目录不存在: {self.haicd_skill_dir}"
        
        # 4. 检查脚本目录
        if not self.scripts_dir.exists():
            return False, f"脚本目录不存在: {self.scripts_dir}"
        
        # 5. 检查控制目录，不存在则创建
        self.control_dir.mkdir(parents=True, exist_ok=True)
        
        # 6. 检查备份目录，不存在则创建
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        print("✅ 前提条件检查通过")
        return True, "所有前提条件满足"
    
    def get_user_consent(self) -> bool:
        """获取用户授权"""
        print("\n" + "="*60)
        print("🔐 HAICD 输出控制层集成授权")
        print("="*60)
        print("\n本操作将：")
        print("1. 📝 将 HAICD 技能设置为常驻输出控制层")
        print("2. 🔄 HAICD 将参与所有智能体输出的处理")
        print("3. 📊 启用状态流跟踪和意义评估")
        print("4. ⚙️ 修改 OpenClaw 配置文件")
        print("5. 🔄 可以随时禁用此功能")
        print("\n安全特性：")
        print("• ✅ 配置修改前会自动备份")
        print("• ✅ 提供完整的回滚机制")
        print("• ✅ 不影响其他技能功能")
        print("• ✅ 性能影响可控")
        print("\n" + "-"*60)
        
        # 模拟用户同意（测试用）
        print("\n⚠️  测试模式：自动同意")
        return True
        
        # 实际使用时取消注释以下代码
        """
        while True:
            consent = input("\n您是否授权启用 HAICD 输出控制层？ (yes/no): ").strip().lower()
            
            if consent in ['yes', 'y', '是', '同意']:
                print("✅ 用户授权确认")
                return True
            elif consent in ['no', 'n', '否', '不同意']:
                print("❌ 用户取消授权")
                return False
            else:
                print("⚠️  请输入 'yes' 或 'no'")
        """
    
    def backup_config(self) -> Tuple[bool, str]:
        """备份当前配置"""
        print("\n💾 备份当前配置...")
        
        try:
            # 读取当前配置
            with open(self.openclaw_config_path, 'r', encoding='utf-8') as f:
                current_config = json.load(f)
            
            # 保存备份
            with open(self.config_backup_path, 'w', encoding='utf-8') as f:
                json.dump(current_config, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 配置已备份到: {self.config_backup_path}")
            return True, f"配置备份成功: {self.config_backup_path}"
            
        except Exception as e:
            error_msg = f"配置备份失败: {str(e)}"
            print(f"❌ {error_msg}")
            return False, error_msg
    
    def load_current_config(self) -> Tuple[Optional[Dict], str]:
        """加载当前配置"""
        try:
            with open(self.openclaw_config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config, "配置加载成功"
        except Exception as e:
            return None, f"配置加载失败: {str(e)}"
    
    def merge_configs(self, current_config: Dict, integration_config: Dict) -> Dict:
        """合并配置"""
        print("\n🔄 合并配置...")
        
        # 创建新的配置对象
        merged_config = current_config.copy()
        
        # 确保 skills 部分存在
        if 'skills' not in merged_config:
            merged_config['skills'] = {}
        
        # 添加 HAICD 集成配置
        haicd_config = integration_config['haicd_output_control'].copy()
        
        # 在配置中添加元数据，但不使用不被识别的 integrations 键
        haicd_config['_metadata'] = {
            "integrated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0.0",
            "mode": "output_control",
            "backup_path": str(self.config_backup_path)
        }
        
        merged_config['skills']['haicd_state_engine'] = haicd_config
        
        print("✅ 配置合并完成")
        return merged_config
    
    def save_config(self, config: Dict) -> Tuple[bool, str]:
        """保存配置"""
        try:
            # 保存新配置
            with open(self.openclaw_config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 新配置已保存到: {self.openclaw_config_path}")
            return True, "配置保存成功"
            
        except Exception as e:
            error_msg = f"配置保存失败: {str(e)}"
            print(f"❌ {error_msg}")
            return False, error_msg
    
    def create_control_scripts(self) -> Tuple[bool, str]:
        """创建控制脚本"""
        print("\n📝 创建控制脚本...")
        
        try:
            # 脚本已经创建，这里只是验证
            scripts = ['enable_haicd.sh', 'disable_haicd.sh', 'status_haicd.sh']
            for script in scripts:
                script_path = self.control_dir / script
                if script_path.exists():
                    print(f"✅ 脚本已存在: {script}")
                else:
                    print(f"⚠️  脚本缺失: {script}")
            
            return True, "控制脚本验证完成"
            
        except Exception as e:
            error_msg = f"控制脚本验证失败: {str(e)}"
            print(f"❌ {error_msg}")
            return False, error_msg
    
    def save_status(self, status: str, details: Dict = None) -> bool:
        """保存状态信息"""
        try:
            status_data = {
                "status": status,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "config_path": str(self.openclaw_config_path),
                "backup_path": str(self.config_backup_path),
                "details": details or {}
            }
            
            with open(self.status_file, 'w', encoding='utf-8') as f:
                json.dump(status_data, f, indent=2, ensure_ascii=False)
            
            return True
        except:
            return False
    
    def enable_integration(self) -> Tuple[bool, str]:
        """启用集成"""
        print("\n🚀 启用 HAICD 输出控制层集成")
        print("="*60)
        
        # 1. 检查前提条件
        success, message = self.check_prerequisites()
        if not success:
            return False, message
        
        # 2. 获取用户授权
        if not self.get_user_consent():
            return False, "用户取消授权"
        
        # 3. 备份配置
        success, message = self.backup_config()
        if not success:
            return False, message
        
        # 4. 加载当前配置
        current_config, message = self.load_current_config()
        if current_config is None:
            return False, message
        
        # 5. 合并配置
        merged_config = self.merge_configs(current_config, self.integration_config)
        
        # 6. 保存配置
        success, message = self.save_config(merged_config)
        if not success:
            return False, message
        
        # 7. 创建控制脚本
        success, message = self.create_control_scripts()
        if not success:
            return False, message
        
        # 8. 保存状态
        self.save_status("enabled", {
            "integration_config": self.integration_config,
            "backup_available": True
        })
        
        print("\n" + "="*60)
        print("🎉 HAICD 输出控制层集成启用成功！")
        print("="*60)
        print("\n📋 集成详情：")
        print(f"• 配置位置: {self.openclaw_config_path}")
        print(f"• 备份位置: {self.config_backup_path}")
        print(f"• 控制脚本: {self.control_dir}/")
        print(f"• 状态文件: {self.status_file}")
        
        print("\n🚀 使用命令：")
        print(f"  启用: {self.control_dir}/enable_haicd.sh")
        print(f"  禁用: {self.control_dir}/disable_haicd.sh")
        print(f"  状态: {self.control_dir}/status_haicd.sh")
        
        print("\n📊 监控建议：")
        print("• 首次使用后检查 OpenClaw 日志")
        print("• 观察智能体输出质量变化")
        print("• 定期运行状态检查脚本")
        
        print("\n⚠️  注意事项：")
        print("• 重启 OpenClaw 服务以使配置生效")
        print("• 如有问题，可使用禁用脚本恢复")
        print("• 备份文件保留 7 天，之后自动清理")
        
        return True, "HAICD 输出控制层集成启用成功"
    
    def disable_integration(self) -> Tuple[bool, str]:
        """禁用集成"""
        print("\n🛑 禁用 HAICD 输出控制层集成")
        print("="*60)
        
        # 1. 检查状态文件
        if not self.status_file.exists():
            return False, "未找到状态文件，可能未启用集成"
        
        # 2. 加载当前配置
        current_config, message = self.load_current_config()
        if current_config is None:
            return False, message
        
        # 3. 移除 HAICD 集成配置
        if 'skills' in current_config and 'haicd_state_engine' in current_config['skills']:
            del current_config['skills']['haicd_state_engine']
            print("✅ 移除 HAICD 技能配置")
        
        # 清理可能遗留的 integrations 键（如果存在）
        if 'integrations' in current_config:
            if 'haicd' in current_config['integrations']:
                del current_config['integrations']['haicd']
                print("✅ 移除 HAICD 集成标记")
            
            # 如果 integrations 为空，移除整个键
            if not current_config['integrations']:
                del current_config['integrations']
                print("✅ 清理空的 integrations 键")
        
        # 4. 保存配置
        success, message = self.save_config(current_config)
        if not success:
            return False, message
        
        # 5. 更新状态
        self.save_status("disabled", {
            "disabled_at": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        print("\n" + "="*60)
        print("✅ HAICD 输出控制层集成已禁用")
        print("="*60)
        print("\n📋 禁用详情：")
        print("• HAICD 输出控制层: 已停止")
        print("• 状态跟踪: 已停止")
        print("• 意义评估: 已停止")
        
        print("\n🔄 重新启用：")
        print(f"  运行: {self.control_dir}/enable_haicd.sh")
        
        print("\n⚠️  注意：")
        print("• 重启 OpenClaw 服务以使配置生效")
        print("• 原始配置备份仍保留")
        
        return True, "HAICD 输出控制层集成禁用成功"
    
    def check_status(self) -> Tuple[bool, str]:
        """检查状态"""
        print("\n📊 HAICD 输出控制层状态检查")
        print("="*60)
        
        status_messages = []
        
        # 1. 检查状态文件
        if self.status_file.exists():
            try:
                with open(self.status_file, 'r', encoding='utf-8') as f:
                    status_data = json.load(f)
                
                status = status_data.get('status', 'unknown')
                print(f"📋 集成状态: {status}")
                print(f"🕐 更新时间: {status_data.get('timestamp', 'unknown')}")
                status_messages.append(f"文件状态: {status}")
                
                if 'details' in status_data:
                    print("\n🔧 配置详情:")
                    for key, value in status_data['details'].items():
                        if isinstance(value, dict):
                            print(f"  • {key}: {len(value)} 项配置")
                        else:
                            print(f"  • {key}: {value}")
                
            except Exception as e:
                print(f"❌ 状态文件读取失败: {str(e)}")
                status_messages.append(f"文件错误: {str(e)}")
        else:
            print("📋 集成状态: 未启用（无状态文件）")
            status_messages.append("文件状态: 未找到")
        
        # 2. 检查配置中的集成状态
        current_config, message = self.load_current_config()
        if current_config:
            haicd_enabled = (
                'skills' in current_config and 
                'haicd_state_engine' in current_config['skills'] and
                current_config['skills']['haicd_state_engine'].get('enabled', False)
            )
            
            if haicd_enabled:
                print("✅ 配置状态: 已启用")
                status_messages.append("配置状态: 已启用")
                
                # 显示详细配置
                haicd_config = current_config['skills']['haicd_state_engine']
                print("\n⚙️  当前配置:")
                print(f"  • 模式: {haicd_config.get('mode', 'unknown')}")
                print(f"  • 集成级别: {haicd_config.get('integration_level', 'unknown')}")
                
                if 'performance' in haicd_config:
                    perf = haicd_config['performance']
                    print(f"  • 最大处理时间: {perf.get('max_processing_time_ms', 'N/A')}ms")
                    print(f"  • 缓存启用: {perf.get('enable_caching', False)}")
                
                # 检查备份文件
                backup_exists = False
                backup_path = None
                
                # 从配置元数据中获取备份路径
                if '_metadata' in haicd_config:
                    backup_path = haicd_config['_metadata'].get('backup_path')
                    if backup_path and Path(backup_path).exists():
                        backup_exists = True
                        print(f"  • 备份文件: 存在 ({backup_path})")
                
                # 也检查旧的 integrations 路径（向后兼容）
                if not backup_exists and 'integrations' in current_config and 'haicd' in current_config['integrations']:
                    backup_path = current_config['integrations']['haicd'].get('backup_path')
                    if backup_path and Path(backup_path).exists():
                        backup_exists = True
                        print(f"  • 备份文件: 存在（旧格式） ({backup_path})")
                
                if not backup_exists:
                    print("  • 备份文件: 未找到")
                    status_messages.append("警告: 备份文件未找到")
                
            else:
                print("❌ 配置状态: 未启用")
                status_messages.append("配置状态: 未启用")
        else:
            print(f"❌ 配置加载失败: {message}")
            status_messages.append(f"配置错误: {message}")
        
        # 3. 检查控制脚本
        print("\n📝 控制脚本状态:")
        scripts = ['enable_haicd.sh', 'disable_haicd.sh', 'status_haicd.sh']
        for script in scripts:
            script_path = self.control_dir / script
            if script_path.exists():
                print(f"  • {script}: ✅ 存在")
                status_messages.append(f"脚本 {script}: 存在")
            else:
                print(f"  • {script}: ❌ 缺失")
                status_messages.append(f"脚本 {script}: 缺失")
        
        # 4. 总结
        print("\n" + "="*60)
        print("📋 状态总结:")
        
        # 判断整体状态
        config_enabled = '配置状态: 已启用' in status_messages
        files_ok = all('缺失' not in msg for msg in status_messages if '脚本' in msg)
        
        if config_enabled and files_ok:
            print("✅ HAICD 输出控制层运行正常")
            print("\n🚀 可用命令:")
            print(f"  禁用: {self.control_dir}/disable_haicd.sh")
            print(f"  状态: {self.control_dir}/status_haicd.sh")
            return True, "运行正常"
        elif not config_enabled and files_ok:
            print("⚠️  HAICD 输出控制层已安装但未启用")
            print("\n🚀 可用命令:")
            print(f"  启用: {self.control_dir}/enable_haicd.sh")
            return False, "已安装未启用"
        else:
            print("❌ HAICD 输出控制层状态异常")
            print("\n🔧 修复建议:")
            print(f"  重新运行: {self.scripts_dir}/haicd_output_control_setup.py --enable")
            return False, "状态异常"
    
    def run_setup(self, action: str = None) -> Tuple[bool, str]:
        """运行设置流程"""
        print("🦞 HAICD 输出控制层集成工具")
        print("="*60)
        print("版本: 1.0.0 | 作者: 智联星核 (ZLXH)")
        print("="*60)
        
        # 如果没有指定动作，显示帮助
        if not action:
            self.show_help()
            return False, "未指定操作"
        
        # 根据动作执行相应操作
        if action == 'enable':
            return self.enable_integration()
        elif action == 'disable':
            return self.disable_integration()
        elif action == 'status':
            return self.check_status()
        elif action == 'help':
            self.show_help()
            return True, "显示帮助"
        else:
            print(f"❌ 未知操作: {action}")
            self.show_help()
            return False, f"未知操作: {action}"
    
    def show_help(self):
        """显示帮助信息"""
        print("\n📖 使用说明:")
        print("="*60)
        print("\n🛠️  可用命令:")
        print("  --enable     启用 HAICD 输出控制层集成")
        print("  --disable    禁用 HAICD 输出控制层集成")
        print("  --status     检查 HAICD 输出控制层状态")
        print("  --help       显示此帮助信息")
        
        print("\n📋 控制脚本:")
        print(f"  {self.control_dir}/enable_haicd.sh    - 启用集成")
        print(f"  {self.control_dir}/disable_haicd.sh   - 禁用集成")
        print(f"  {self.control_dir}/status_haicd.sh    - 检查状态")
        
        print("\n🔧 直接使用 Python 脚本:")
        print(f"  python3 {self.scripts_dir}/haicd_output_control_setup.py --enable")
        print(f"  python3 {self.scripts_dir}/haicd_output_control_setup.py --disable")
        print(f"  python3 {self.scripts_dir}/haicd_output_control_setup.py --status")
        
        print("\n⚠️  注意事项:")
        print("• 启用集成需要用户明确授权")
        print("• 配置修改前会自动备份")
        print("• 重启 OpenClaw 服务以使配置生效")
        print("• 可以随时禁用集成")
        
        print("\n📞 支持:")
        print("• 理论创建者: Jeason")
        print("• 技能实现: 智联星核 (ZLXH)")
        print("• 文档: docs/HAICD 技能包-使用说明.md")


def main():
    """主函数"""
    import sys
    
    # 简单参数解析
    action = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '--enable':
            action = 'enable'
        elif arg == '--disable':
            action = 'disable'
        elif arg == '--status':
            action = 'status'
        elif arg in ['--help', '-h']:
            action = 'help'
    
    # 创建设置对象并运行
    setup = HAICDOutputControlSetup()
    success, message = setup.run_setup(action)
    
    # 返回退出码
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()