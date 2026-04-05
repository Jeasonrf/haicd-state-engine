#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HAICD 引擎集成层
Human-AI Interaction Contextual Dynamics Model
Integrated Engine - 状态选择与状态流跟踪的统一接口

作者：Jeason (理论创建者), 智联星核 (ZLXH)
版本：v1.0.0
许可：CC BY-NC-SA 4.0

核心逻辑：
1. A 脚本 (haicd-scoring-system.py) 提供状态选择和意义评估能力
2. B 脚本 (state_flow_tracker.py) 提供状态流跟踪能力
3. 本集成层负责：
   - 从 A 获取 B 所需的初始设定/初始状态
   - 若 A 中找不到 B 所需参数，B 根据人机交互上下文 +LLM 领域知识经验判定
   - 每次对话前，完成上次及历次对话的综合判定
   - 以逻辑/事件/场景一致的相近对话状态为核心依据，推理计算状态流动态赋值
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

# 导入 A 脚本：评分系统
from haicd_scoring_system import (
    MeaningEvaluator,
    StateSelector,
    StateDefinition,
    StateName,
    STATES,
    get_scenario_config
)

# 导入 B 脚本：状态流跟踪器
from state_flow_tracker import StateFlowTracker


# ==================== 集成引擎 ====================

class HAICDEngine:
    """
    HAICD 集成引擎
    
    统一状态选择和状态流跟踪，实现：
    1. 从评分系统获取初始状态
    2. 基于历史状态流动态调整
    3. 跨对话状态一致性推理
    """
    
    def __init__(
        self,
        session_id: str,
        scenario: str = 'default',
        storage_path: str = "~/.openclaw/skills/haicd-state-engine/state_flow.json"
    ):
        """
        初始化引擎
        
        Args:
            session_id: 当前会话 ID
            scenario: 场景名称（用于加载权重配置）
            storage_path: 状态流存储路径
        """
        self.session_id = session_id
        self.scenario = scenario
        
        # 加载场景配置
        self.scenario_config = get_scenario_config(scenario)
        
        # 初始化 A 脚本：评分系统
        weights = self.scenario_config.get('weights')
        self.evaluator = MeaningEvaluator(weights)
        self.selector = StateSelector(self.evaluator)
        
        # 初始化 B 脚本：状态流跟踪器
        self.tracker = StateFlowTracker(session_id, storage_path)
        
        # 状态流动态参数
        self.state_flow_params = self._init_state_flow_params()
    
    def _init_state_flow_params(self) -> Dict:
        """
        初始化状态流参数
        
        优先级：
        1. 从历史状态流推理（最近 N 次相似场景）
        2. 从 A 脚本评分系统获取推荐
        3. 使用默认参数
        """
        # 从历史状态流获取最近状态
        recent_history = self.tracker.get_state_history(limit=10)
        
        # 分析历史状态分布
        state_distribution = self._analyze_state_distribution(recent_history)
        
        # 检测异常
        anomalies = self.tracker.detect_anomalies()
        
        # 推理状态流参数
        params = {
            'current_state': self.tracker.get_current_state(),
            'recent_states': [h['state'] for h in recent_history],
            'state_distribution': state_distribution,
            'anomalies': anomalies,
            'consistency_score': self._calc_consistency_score(recent_history),
            'scenario_match': self._find_similar_scenarios(recent_history)
        }
        
        return params
    
    def _analyze_state_distribution(self, history: List[Dict]) -> Dict[str, int]:
        """分析状态分布"""
        distribution = {}
        for record in history:
            state = record.get('state', 'Unknown')
            distribution[state] = distribution.get(state, 0) + 1
        return distribution
    
    def _calc_consistency_score(self, history: List[Dict]) -> float:
        """
        计算状态一致性得分
        
        得分越高表示历史状态越稳定
        """
        if len(history) < 2:
            return 1.0  # 历史记录不足，认为一致
        
        states = [h['state'] for h in history]
        unique_count = len(set(states))
        total_count = len(states)
        
        # 一致性 = 1 - (唯一状态数 / 总状态数)
        consistency = 1.0 - (unique_count / total_count)
        return max(0.0, min(1.0, consistency))
    
    def _find_similar_scenarios(self, history: List[Dict]) -> List[Dict]:
        """
        查找相似场景的历史记录
        
        基于场景、用户角色、任务阶段匹配
        """
        similar = []
        current_scenario = self.scenario_config.get('scenario', 'general')
        current_user_role = self.scenario_config.get('user_role', '通用用户')
        
        for record in history:
            context = record.get('context', {})
            record_scenario = context.get('scenario', 'general')
            record_user_role = context.get('user_role', '通用用户')
            
            # 计算相似度
            scenario_match = 1.0 if record_scenario == current_scenario else 0.5
            role_match = 1.0 if record_user_role == current_user_role else 0.5
            
            similarity = (scenario_match + role_match) / 2.0
            
            if similarity >= 0.5:
                similar.append({
                    'state': record['state'],
                    'timestamp': record['timestamp'],
                    'similarity': similarity
                })
        
        # 按相似度排序
        similar.sort(key=lambda x: x['similarity'], reverse=True)
        return similar[:5]  # 返回最相似的 5 条
    
    def select_state_with_history(
        self,
        context: Dict,
        top_k: int = 3,
        use_history: bool = True
    ) -> List[Tuple[StateDefinition, Any]]:
        """
        结合历史状态流选择最优状态
        
        Args:
            context: 当前上下文信息
            top_k: 返回前 k 个推荐
            use_history: 是否使用历史状态流调整
        
        Returns:
            状态和评分的列表（包含历史调整因子）
        """
        # 步骤 1：使用 A 脚本进行基础评分
        base_recommendations = self.selector.select(context, top_k=top_k * 2)
        
        if not use_history or not base_recommendations:
            return base_recommendations[:top_k]
        
        # 步骤 2：基于历史状态流调整评分
        adjusted_recommendations = []
        
        for state, score in base_recommendations:
            # 计算历史调整因子
            history_factor = self._calc_history_factor(state.name)
            
            # 调整总分
            adjusted_total = score.total_score * (1.0 + history_factor)
            
            # 创建调整后的评分对象
            adjusted_score = {
                'original_score': score.total_score,
                'history_factor': history_factor,
                'adjusted_score': adjusted_total,
                'level': score.level,
                'recommendation': score.recommendation
            }
            
            adjusted_recommendations.append((state, adjusted_score))
        
        # 步骤 3：按调整后得分排序
        adjusted_recommendations.sort(
            key=lambda x: x[1]['adjusted_score'],
            reverse=True
        )
        
        return adjusted_recommendations[:top_k]
    
    def _calc_history_factor(self, state_name: str) -> float:
        """
        计算历史调整因子
        
        基于：
        1. 该状态在历史中的出现频率
        2. 该状态在相似场景中的表现
        3. 状态切换的稳定性
        
        Returns:
            调整因子 (-0.3 ~ +0.3)
        """
        factor = 0.0
        
        # 因素 1：历史出现频率
        distribution = self.state_flow_params['state_distribution']
        total_records = sum(distribution.values())
        if total_records > 0:
            freq = distribution.get(state_name, 0) / total_records
            # 高频状态给予小幅正向调整
            factor += freq * 0.15
        
        # 因素 2：相似场景匹配
        similar_scenarios = self.state_flow_params['scenario_match']
        for sim in similar_scenarios:
            if sim['state'] == state_name:
                factor += sim['similarity'] * 0.15
        
        # 因素 3：一致性惩罚（频繁切换状态）
        anomalies = self.state_flow_params['anomalies']
        for anomaly in anomalies.get('anomalies', []):
            if anomaly['type'] == 'frequent_switch':
                factor -= 0.1  # 频繁切换惩罚
        
        # 限制调整因子范围
        return max(-0.3, min(0.3, factor))
    
    def record_and_track(
        self,
        state_name: str,
        context: Dict,
        output_quality: Optional[float] = None
    ) -> Dict:
        """
        记录状态并跟踪效果
        
        Args:
            state_name: 使用的状态名称
            context: 上下文信息
            output_quality: 输出质量评分（可选，用于后续优化）
        
        Returns:
            跟踪报告
        """
        # 记录到状态流
        self.tracker.record_state(state_name, context)
        
        # 生成跟踪报告
        report = {
            'state': state_name,
            'timestamp': datetime.now().isoformat(),
            'context_summary': {
                'scenario': context.get('scenario', 'general'),
                'user_role': context.get('user_role', '通用用户'),
                'risk_level': context.get('risk_level', 'medium')
            },
            'output_quality': output_quality,
            'current_flow_params': {
                'consistency_score': self.state_flow_params['consistency_score'],
                'recent_states_count': len(self.state_flow_params['recent_states']),
                'anomalies_count': len(self.state_flow_params['anomalies'].get('anomalies', []))
            }
        }
        
        # 更新状态流参数
        self.state_flow_params = self._init_state_flow_params()
        
        return report
    
    def get_comprehensive_analysis(self) -> Dict:
        """
        获取综合分析结果
        
        包含：
        1. 当前状态
        2. 历史状态流分析
        3. 状态切换模式
        4. 推荐优化建议
        
        Returns:
            综合分析报告
        """
        current_state = self.tracker.get_current_state()
        history = self.tracker.get_state_history(limit=20)
        anomalies = self.tracker.detect_anomalies()
        
        # 分析状态切换模式
        switch_pattern = self._analyze_switch_pattern(history)
        
        # 生成优化建议
        recommendations = self._generate_recommendations(
            current_state, history, anomalies, switch_pattern
        )
        
        return {
            'session_id': self.session_id,
            'current_state': current_state,
            'history_summary': {
                'total_records': len(history),
                'unique_states': len(set(h['state'] for h in history)),
                'consistency_score': self.state_flow_params['consistency_score']
            },
            'state_distribution': self.state_flow_params['state_distribution'],
            'switch_pattern': switch_pattern,
            'anomalies': anomalies,
            'similar_scenarios': self.state_flow_params['scenario_match'],
            'recommendations': recommendations
        }
    
    def _analyze_switch_pattern(self, history: List[Dict]) -> Dict:
        """分析状态切换模式"""
        if len(history) < 2:
            return {'pattern': 'insufficient_data', 'description': '历史记录不足'}
        
        states = [h['state'] for h in history]
        
        # 检测切换频率
        switches = sum(1 for i in range(1, len(states)) if states[i] != states[i-1])
        switch_rate = switches / (len(states) - 1)
        
        # 判断模式
        if switch_rate < 0.2:
            pattern = 'stable'
            description = '状态稳定，很少切换'
        elif switch_rate < 0.5:
            pattern = 'moderate'
            description = '适度切换，响应场景变化'
        else:
            pattern = 'frequent'
            description = '频繁切换，可能缺乏一致性'
        
        return {
            'pattern': pattern,
            'description': description,
            'switch_rate': round(switch_rate, 3),
            'total_switches': switches
        }
    
    def _generate_recommendations(
        self,
        current_state: Optional[str],
        history: List[Dict],
        anomalies: Dict,
        switch_pattern: Dict
    ) -> List[str]:
        """生成优化建议"""
        recommendations = []
        
        # 基于异常检测
        for anomaly in anomalies.get('anomalies', []):
            if anomaly['type'] == 'frequent_switch':
                recommendations.append(
                    "⚠️ 检测到频繁状态切换，建议增加状态稳定性阈值"
                )
            elif anomaly['type'] == 'stagnation':
                recommendations.append(
                    "💡 检测到状态停滞，建议主动探索新状态"
                )
        
        # 基于切换模式
        if switch_pattern['pattern'] == 'frequent':
            recommendations.append(
                "📊 状态切换频繁，建议设置最小状态持续时间"
            )
        elif switch_pattern['pattern'] == 'stable':
            recommendations.append(
                "✅ 状态稳定，保持一致性"
            )
        
        # 基于当前状态
        if current_state:
            if current_state in ['幻觉', '高风险创新', '概念探索']:
                recommendations.append(
                    "🎨 当前为创新状态，注意标注不确定性"
                )
            elif current_state in ['顺应', '经验驱动型', '实践验证型']:
                recommendations.append(
                    "✅ 当前为稳定状态，适合执行关键任务"
                )
        
        if not recommendations:
            recommendations.append("状态流健康，无需特殊调整")
        
        return recommendations


# ==================== 快捷接口函数 ====================

def create_engine(
    session_id: str,
    scenario: str = 'default'
) -> HAICDEngine:
    """
    创建 HAICD 引擎实例
    
    Args:
        session_id: 会话 ID
        scenario: 场景名称
    
    Returns:
        HAICDEngine 实例
    """
    return HAICDEngine(session_id, scenario)


def select_best_state(
    session_id: str,
    context: Dict,
    scenario: str = 'default'
) -> Tuple[str, Dict]:
    """
    选择最优状态（快捷函数）
    
    Args:
        session_id: 会话 ID
        context: 上下文信息
        scenario: 场景名称
    
    Returns:
        (最佳状态名称，评分详情)
    """
    engine = HAICDEngine(session_id, scenario)
    recommendations = engine.select_state_with_history(context, top_k=1)
    
    if recommendations:
        state, score = recommendations[0]
        return state.name, score
    else:
        return '顺应', {'error': '无法选择状态'}


def track_state(
    session_id: str,
    state_name: str,
    context: Dict,
    scenario: str = 'default'
) -> Dict:
    """
    跟踪状态（快捷函数）
    
    Args:
        session_id: 会话 ID
        state_name: 状态名称
        context: 上下文信息
        scenario: 场景名称
    
    Returns:
        跟踪报告
    """
    engine = HAICDEngine(session_id, scenario)
    return engine.record_and_track(state_name, context)


# ==================== 主程序（演示） ====================

def main():
    """演示集成引擎用法"""
    print("=" * 60)
    print("HAICD 集成引擎演示")
    print("=" * 60)
    
    # 创建引擎
    engine = HAICDEngine(
        session_id="demo-session-001",
        scenario="academic_research"
    )
    
    # 演示 1：选择状态（结合历史）
    print("\n【演示 1】选择最优状态（结合历史状态流）")
    context = {
        'user_role': '科研工作者',
        'scenario': 'innovation',
        'risk_level': 'high'
    }
    
    recommendations = engine.select_state_with_history(context, top_k=3)
    for i, (state, score) in enumerate(recommendations, 1):
        print(f"\n{i}. {state.name}")
        print(f"   原始评分：{score['original_score']:.3f}")
        print(f"   历史调整因子：{score['history_factor']:+.3f}")
        print(f"   调整后评分：{score['adjusted_score']:.3f}")
    
    # 演示 2：记录状态
    print("\n【演示 2】记录状态到状态流")
    if recommendations:
        best_state = recommendations[0][0].name
        report = engine.record_and_track(best_state, context, output_quality=0.85)
        print(f"已记录状态：{report['state']}")
        print(f"时间戳：{report['timestamp']}")
    
    # 演示 3：综合分析
    print("\n【演示 3】综合分析状态流")
    analysis = engine.get_comprehensive_analysis()
    print(f"当前状态：{analysis['current_state']}")
    print(f"历史记录数：{analysis['history_summary']['total_records']}")
    print(f"状态一致性：{analysis['history_summary']['consistency_score']:.3f}")
    print(f"切换模式：{analysis['switch_pattern']['description']}")
    
    print("\n优化建议:")
    for rec in analysis['recommendations']:
        print(f"  {rec}")
    
    print("\n" + "=" * 60)
    print("演示完成")
    print("=" * 60)


if __name__ == '__main__':
    main()
