#!/usr/bin/env python3
"""
HAICD 输出处理器
集成到智能体输出管道的中间件

功能：处理智能体输出，应用 HAICD 状态选择和意义评估
作者：智联星核 (ZLXH)
日期：2026-04-06
版本：v1.0.0
"""

import json
import time
import logging
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProcessingMode(Enum):
    """处理模式"""
    RESIDENT = "resident"          # 常驻模式，处理所有输出
    SELECTIVE = "selective"       # 选择性处理，根据条件触发
    MANUAL = "manual"             # 手动模式，显式调用


class OutputQuality(Enum):
    """输出质量等级"""
    EXCELLENT = "excellent"       # 优秀：完全匹配预期且超出预期
    GOOD = "good"                 # 良好：满足需求，有额外价值
    ACCEPTABLE = "acceptable"     # 可接受：基本满足需求
    NEEDS_IMPROVEMENT = "needs_improvement"  # 需要改进：有缺陷但可用
    POOR = "poor"                 # 差：不满足需求


@dataclass
class ProcessingMetrics:
    """处理指标"""
    total_processed: int = 0
    total_processing_time_ms: float = 0.0
    avg_processing_time_ms: float = 0.0
    max_processing_time_ms: float = 0.0
    state_changes: int = 0
    quality_distribution: Dict[str, int] = None
    
    def __post_init__(self):
        if self.quality_distribution is None:
            self.quality_distribution = {level.value: 0 for level in OutputQuality}
    
    def record_processing(self, processing_time_ms: float, quality: OutputQuality):
        """记录处理指标"""
        self.total_processed += 1
        self.total_processing_time_ms += processing_time_ms
        self.avg_processing_time_ms = self.total_processing_time_ms / self.total_processed
        self.max_processing_time_ms = max(self.max_processing_time_ms, processing_time_ms)
        self.quality_distribution[quality.value] += 1
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return asdict(self)


@dataclass
class ProcessingContext:
    """处理上下文"""
    user_role: str
    scenario: str
    risk_level: str
    conversation_history: List[Dict] = None
    user_preferences: Dict[str, Any] = None
    system_constraints: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.conversation_history is None:
            self.conversation_history = []
        if self.user_preferences is None:
            self.user_preferences = {}
        if self.system_constraints is None:
            self.system_constraints = {}


class HAICDOutputProcessor:
    """HAICD 输出处理器"""
    
    def __init__(self, config_path: str = None, mode: ProcessingMode = ProcessingMode.RESIDENT):
        """
        初始化输出处理器
        
        Args:
            config_path: 配置文件路径
            mode: 处理模式
        """
        self.mode = mode
        self.metrics = ProcessingMetrics()
        self.state_flow_tracker = None
        self.meaning_evaluator = None
        self.context_analyzer = None
        
        # 加载配置
        self.config = self._load_config(config_path)
        
        # 初始化组件
        self._initialize_components()
        
        logger.info(f"HAICD 输出处理器初始化完成，模式: {mode.value}")
    
    def _load_config(self, config_path: str) -> Dict:
        """加载配置"""
        default_config = {
            "processing": {
                "max_processing_time_ms": 100,
                "enable_caching": True,
                "cache_ttl_seconds": 300,
                "quality_thresholds": {
                    "excellent": 0.9,
                    "good": 0.7,
                    "acceptable": 0.5,
                    "needs_improvement": 0.3
                }
            },
            "state_selection": {
                "top_k": 3,
                "confidence_threshold": 0.6,
                "fallback_state": "顺应"
            },
            "monitoring": {
                "enabled": True,
                "log_level": "info",
                "metrics_collection": True
            }
        }
        
        if config_path and Path(config_path).exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                
                # 合并配置
                self._merge_configs(default_config, user_config)
                logger.info(f"从 {config_path} 加载配置")
                
            except Exception as e:
                logger.warning(f"配置加载失败: {str(e)}，使用默认配置")
        
        return default_config
    
    def _merge_configs(self, base: Dict, overlay: Dict):
        """合并配置"""
        for key, value in overlay.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_configs(base[key], value)
            else:
                base[key] = value
    
    def _initialize_components(self):
        """初始化组件"""
        # 这里会初始化实际的 HAICD 组件
        # 目前使用模拟实现
        
        logger.info("初始化 HAICD 组件...")
        
        # 模拟状态流跟踪器
        self.state_flow_tracker = {
            "track": lambda session_id, state: logger.debug(f"跟踪状态: {state}"),
            "get_history": lambda session_id: [],
            "analyze_patterns": lambda session_id: {}
        }
        
        # 模拟意义评估器
        self.meaning_evaluator = {
            "evaluate": lambda output, context: {
                "user_value": 0.8,
                "cognitive_contribution": 0.7,
                "risk_controlled": 0.9,
                "ethical_compliance": 0.95,
                "total_score": 0.85,
                "level": "meaningful"
            }
        }
        
        # 模拟上下文分析器
        self.context_analyzer = {
            "analyze": lambda context: {
                "user_intent": "information_seeking",
                "emotional_tone": "neutral",
                "complexity_level": "medium",
                "urgency": "normal"
            }
        }
        
        logger.info("HAICD 组件初始化完成")
    
    def should_process(self, context: ProcessingContext) -> bool:
        """
        判断是否需要处理
        
        Args:
            context: 处理上下文
            
        Returns:
            是否需要处理
        """
        if self.mode == ProcessingMode.RESIDENT:
            return True
        
        elif self.mode == ProcessingMode.SELECTIVE:
            # 根据条件判断是否需要处理
            conditions = self.config.get("selective_conditions", {})
            
            # 检查用户角色
            if "user_roles" in conditions:
                if context.user_role not in conditions["user_roles"]:
                    return False
            
            # 检查场景
            if "scenarios" in conditions:
                if context.scenario not in conditions["scenarios"]:
                    return False
            
            # 检查风险等级
            if "risk_levels" in conditions:
                if context.risk_level not in conditions["risk_levels"]:
                    return False
            
            return True
        
        elif self.mode == ProcessingMode.MANUAL:
            # 手动模式需要显式调用
            return False
        
        return False
    
    def process_output(self, raw_output: str, context: ProcessingContext) -> Tuple[str, Dict]:
        """
        处理智能体输出
        
        Args:
            raw_output: 原始输出文本
            context: 处理上下文
            
        Returns:
            Tuple[处理后的输出文本, 处理详情]
        """
        start_time = time.time()
        
        try:
            # 1. 检查是否需要处理
            if not self.should_process(context):
                logger.debug("跳过处理（不满足处理条件）")
                return raw_output, {"processed": False, "reason": "skip_condition"}
            
            # 2. 分析上下文
            context_analysis = self.context_analyzer["analyze"](context)
            logger.debug(f"上下文分析: {context_analysis}")
            
            # 3. 选择状态
            selected_state = self._select_state(context, context_analysis)
            logger.info(f"选择状态: {selected_state}")
            
            # 4. 评估原始输出意义
            meaning_evaluation = self.meaning_evaluator["evaluate"](raw_output, context)
            logger.debug(f"意义评估: {meaning_evaluation}")
            
            # 5. 应用状态调整
            processed_output = self._apply_state_adjustment(raw_output, selected_state, context)
            
            # 6. 评估处理后的输出
            processed_evaluation = self.meaning_evaluator["evaluate"](processed_output, context)
            
            # 7. 跟踪状态流
            self.state_flow_tracker["track"](context.user_role, selected_state)
            
            # 8. 计算处理时间
            processing_time_ms = (time.time() - start_time) * 1000
            
            # 9. 评估输出质量
            quality = self._evaluate_quality(processed_evaluation["total_score"])
            
            # 10. 记录指标
            self.metrics.record_processing(processing_time_ms, quality)
            
            # 11. 检查性能阈值
            if processing_time_ms > self.config["processing"]["max_processing_time_ms"]:
                logger.warning(f"处理时间超过阈值: {processing_time_ms:.2f}ms")
            
            # 12. 生成处理详情
            processing_details = {
                "processed": True,
                "processing_time_ms": processing_time_ms,
                "selected_state": selected_state,
                "original_evaluation": meaning_evaluation,
                "processed_evaluation": processed_evaluation,
                "quality": quality.value,
                "context_analysis": context_analysis,
                "improvement_score": processed_evaluation["total_score"] - meaning_evaluation["total_score"]
            }
            
            logger.info(f"输出处理完成: {processing_time_ms:.2f}ms, 质量: {quality.value}")
            
            return processed_output, processing_details
            
        except Exception as e:
            logger.error(f"输出处理失败: {str(e)}")
            
            # 记录错误指标
            error_time_ms = (time.time() - start_time) * 1000
            self.metrics.record_processing(error_time_ms, OutputQuality.POOR)
            
            # 返回原始输出和错误信息
            return raw_output, {
                "processed": False,
                "error": str(e),
                "processing_time_ms": error_time_ms
            }
    
    def _select_state(self, context: ProcessingContext, context_analysis: Dict) -> str:
        """选择状态"""
        # 这里实现具体的状态选择逻辑
        # 目前使用基于场景的简单规则
        
        state_rules = {
            "academic_research": ["高风险创新", "未来导向型输出", "概念探索"],
            "software_engineering": ["顺应", "经验驱动型", "资源受限下的保守输出"],
            "thought_experiment": ["幻觉", "概念探索", "高风险创新"],
            "emergency_response": ["顺应", "实践验证型", "保守型推理"],
            "brainstorming": ["创新性错误", "探索性思考", "资源受限下的灵感激发"],
            "default": ["顺应", "经验驱动型", "实践验证型"]
        }
        
        # 根据场景选择状态
        scenario = context.scenario
        if scenario in state_rules:
            states = state_rules[scenario]
        else:
            states = state_rules["default"]
        
        # 简单规则：根据风险等级调整
        if context.risk_level == "high":
            # 高风险场景倾向于保守状态
            if "顺应" in states:
                return "顺应"
            elif "保守型推理" in states:
                return "保守型推理"
            else:
                return states[0]
        elif context.risk_level == "low":
            # 低风险场景可以尝试创新状态
            for state in states:
                if "创新" in state or "探索" in state:
                    return state
            return states[0]
        else:
            # 中等风险使用第一个推荐状态
            return states[0]
    
    def _apply_state_adjustment(self, output: str, state: str, context: ProcessingContext) -> str:
        """应用状态调整"""
        # 这里实现具体的状态调整逻辑
        # 目前使用简单的文本调整
        
        adjustment_rules = {
            "顺应": {
                "description": "完全匹配预期且超出预期",
                "adjustment": lambda text: f"{text}\n\n【HAICD状态：顺应】此回复经过优化，确保完全符合您的需求。"
            },
            "高风险创新": {
                "description": "不真实前提 + 严谨过程 + 启发性",
                "adjustment": lambda text: f"{text}\n\n【HAICD状态：高风险创新】请注意：此回复包含创新性假设，建议谨慎验证。"
            },
            "未来导向型输出": {
                "description": "现实不足但启发性强",
                "adjustment": lambda text: f"{text}\n\n【HAICD状态：未来导向型输出】此回复侧重于未来可能性，实际应用需结合当前条件。"
            },
            "保守型推理": {
                "description": "稳定无新颖",
                "adjustment": lambda text: f"{text}\n\n【HAICD状态：保守型推理】此回复采用保守策略，确保安全可靠。"
            },
            "default": {
                "description": "默认调整",
                "adjustment": lambda text: f"{text}\n\n【HAICD状态：{state}】"
            }
        }
        
        if state in adjustment_rules:
            adjustment = adjustment_rules[state]["adjustment"]
        else:
            adjustment = adjustment_rules["default"]["adjustment"]
        
        return adjustment(output)
    
    def _evaluate_quality(self, score: float) -> OutputQuality:
        """评估输出质量"""
        thresholds = self.config["processing"]["quality_thresholds"]
        
        if score >= thresholds["excellent"]:
            return OutputQuality.EXCELLENT
        elif score >= thresholds["good"]:
            return OutputQuality.GOOD
        elif score >= thresholds["acceptable"]:
            return OutputQuality.ACCEPTABLE
        elif score >= thresholds["needs_improvement"]:
            return OutputQuality.NEEDS_IMPROVEMENT
        else:
            return OutputQuality.POOR
    
    def get_processing_stats(self) -> Dict:
        """获取处理统计"""
        return {
            "metrics": self.metrics.to_dict(),
            "config": self.config,
            "mode": self.mode.value,
            "status": "active"
        }
    
    def update_config(self, new_config: Dict):
        """更新配置"""
        self._merge_configs(self.config, new_config)
        logger.info("配置已更新")
    
    def reset_metrics(self):
        """重置指标"""
        self.metrics = ProcessingMetrics()
        logger.info("指标已重置")


def create_processor_from_config(config_file: str = None) -> HAICDOutputProcessor:
    """
    从配置文件创建处理器
    
    Args:
        config_file: 配置文件路径
        
    Returns:
        HAICDOutputProcessor 实例
    """
    if config_file and Path(config_file).exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            mode_str = config.get("processing", {}).get("mode", "resident")
            mode = ProcessingMode(mode_str)
            
            processor = HAICDOutputProcessor(config_file, mode)
            logger.info(f"从配置文件创建处理器: {config_file}")
            
            return processor
            
        except Exception as e:
            logger.error(f"配置文件加载失败: {str(e)}")
    
    # 使用默认配置
    logger.info("使用默认配置创建处理器")
    return HAICDOutputProcessor()


# 演示函数
def demo():
    """演示输出处理器功能"""
    print("🦞 HAICD 输出处理器演示")
    print("="*60)
    
    # 创建处理器
    processor = HAICDOutputProcessor()
    
    # 创建测试上下文
    context = ProcessingContext(
        user_role="科研工作者",
        scenario="academic_research",
        risk_level="high"
    )
    
    # 测试输出
    test_outputs = [
        "根据现有研究，这种治疗方法的效果还不确定，需要更多临床试验验证。",
        "我建议尝试一种全新的治疗方法，虽然风险较高，但可能带来突破性进展。",
        "这个问题比较复杂，我需要更多时间研究才能给出准确回答。"
    ]
    
    for i, raw_output in enumerate(test_outputs, 1):
        print(f"\n📝 测试 {i}:")
        print(f"原始输出: {raw_output}")
        
        processed_output, details = processor.process_output(raw_output, context)
        
        print(f"处理后输出: {processed_output}")
        print(f"处理详情: {json.dumps(details, indent=2, ensure_ascii=False)}")
    
    # 显示统计信息
    print("\n📊 处理统计:")
    stats = processor.get_processing_stats()
    print(json.dumps(stats, indent=2, ensure_ascii=False))
    
    print("\n✅ 演示完成")


if __name__ == "__main__":
    demo()