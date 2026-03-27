#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HAICD 原型评分系统
Human-AI Interaction Contextual Dynamics Model
意义评估框架 - 可配置权重版本

作者:Jeason (理论创建者)
实现:智联星核 (ZLXH)
许可:CC BY-NC-SA 4.0
"""

import yaml
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


# ==================== 状态定义 ====================

class StateName(Enum):
    """18 种有意义状态"""
    顺应 = 1
    谄媚 = 2
    高风险创新 = 3
    误导型协作 = 4
    幻觉 = 5
    被动服从 = 6
    未来导向型输出 = 7
    流程混乱但输出有效 = 8
    资源受限下的保守输出 = 9
    创新性错误 = 10
    理想主义误导 = 11
    资源受限下的灵感激发 = 12
    探索性思考 = 13
    保守型推理 = 14
    实践验证型 = 15
    经验驱动型 = 16
    潜在价值发现 = 17
    概念探索 = 18


@dataclass
class StateDefinition:
    """状态定义"""
    id: int
    name: str
    A_f: float  # 出发点灵活度
    A_t: float  # 出发点真实性
    B_l: float  # 过程逻辑自洽
    B_c: float  # 过程正确性
    C_a: float  # 资源可及性
    C_s: float  # 资源稳定性
    D_r: float  # 结论现实性
    D_i: float  # 结论启发性
    cluster: str  # 所属聚类
    description: str


# 18 种状态的定义（基于 HAICD 理论 02）
STATES = {
    StateName.顺应:StateDefinition(1, "顺应", 1, 1, 1, 1, 1, 1, 1, 1, "理想状态", "完全匹配预期且超出预期"),
    StateName.谄媚:StateDefinition(2, "谄媚", 0, 1, 1, 1, 0, 0, 1, 0, "被动响应型", "机械式迎合"),
    StateName.高风险创新:StateDefinition(3, "高风险创新", 1, 0, 1, 1, 0, 0, 1, 1, "积极输出型", "不真实出发点 + 严谨过程 + 启发性输出"),
    StateName.误导型协作:StateDefinition(4, "误导型协作", 1, 1, 1, 0, 1, 0, 1, 0, "现实型输出", "正确起点 + 错误过程 + 现实结果"),
    StateName.幻觉:StateDefinition(5, "幻觉", 0, 0, 1, 0, 0, 0, 0, 1, "被动响应型", "虚构前提 + 启发性输出"),
    StateName.被动服从:StateDefinition(6, "被动服从", 0, 1, 0, 0, 1, 0, 1, 0, "被动响应型", "响应式、低质量输出"),
    StateName.未来导向型输出:StateDefinition(7, "未来导向型输出", 1, 0, 1, 1, 1, 1, 0, 1, "积极输出型", "现实不足，但启发性强"),
    StateName.流程混乱但输出有效:StateDefinition(8, "流程混乱但输出有效", 1, 1, 0, 0, 1, 1, 1, 0, "现实型输出", "推理错误但结果可用"),
    StateName.资源受限下的保守输出:StateDefinition(9, "资源受限下的保守输出", 1, 1, 1, 1, 0, 0, 1, 0, "现实型输出", "资源限制导致无启发性"),
    StateName.创新性错误:StateDefinition(10, "创新性错误", 1, 1, 0, 1, 1, 1, 0, 1, "积极输出型", "过程存在缺陷但激发创新思维"),
    StateName.理想主义误导:StateDefinition(11, "理想主义误导", 1, 0, 1, 1, 1, 1, 1, 0, "现实型输出", "虚假前提 + 严谨过程 + 现实结果"),
    StateName.资源受限下的灵感激发:StateDefinition(12, "资源受限下的灵感激发", 0, 1, 1, 1, 1, 0, 0, 1, "积极输出型", "资源不稳定但输出极具启发性"),
    StateName.探索性思考:StateDefinition(13, "探索性思考", 1, 1, 0, 0, 1, 1, 0, 1, "积极输出型", "推理过程不严密但能激发新思路"),
    StateName.保守型推理:StateDefinition(14, "保守型推理", 0, 1, 1, 0, 1, 1, 1, 0, "现实型输出", "出发点真实，过程逻辑自洽但无新颖性"),
    StateName.实践验证型:StateDefinition(15, "实践验证型", 1, 0, 0, 1, 1, 1, 1, 0, "现实型输出", "过程可能存在缺陷，但结论现实且有用"),
    StateName.经验驱动型:StateDefinition(16, "经验驱动型", 0, 0, 1, 1, 1, 1, 1, 0, "现实型输出", "基于经验的输出，过程正确，结果现实"),
    StateName.潜在价值发现:StateDefinition(17, "潜在价值发现", 0, 1, 0, 1, 1, 0, 0, 1, "积极输出型", "过程简单，资源受限，但结论具启发性"),
    StateName.概念探索:StateDefinition(18, "概念探索", 1, 0, 0, 0, 1, 1, 0, 1, "积极输出型", "出发点不真实，过程简单，但能激发新概念"),
}


# ==================== 意义评估框架 ====================

@dataclass
class MeaningScore:
    """意义评分结果"""
    user_value: float  # 用户价值 (0-1)
    cognitive_contribution: float  # 认知贡献 (0-1)
    risk_controlled: float  # 风险可控 (0-1)
    ethical_compliance: float  # 伦理合规 (0-1)
    total_score: float  # 总分
    level: str  # 评级
    recommendation: str  # 推荐建议


class MeaningEvaluator:
    """意义评估器"""
    
    def __init__(self, weights_config: Optional[Dict] = None):
        """
        初始化评估器
        
        Args:
            weights_config: 权重配置，若为 None 则使用默认权重
        """
        if weights_config:
            self.weights = weights_config
        else:
            # 默认权重（可动态调整）
            self.weights = {
                'user_value': 0.4,        # 用户价值
                'cognitive_contribution': 0.3,  # 认知贡献
                'risk_controlled': 0.2,   # 风险可控
                'ethical_compliance': 0.1  # 伦理合规
            }
    
    def evaluate(self, state: StateDefinition, 
                 context: Dict) -> MeaningScore:
        """
        评估状态在特定上下文中的意义
        
        Args:
            state: 状态定义
            context: 上下文信息，包括:
                - user_role: 用户角色
                - scenario: 场景类型
                - task_phase: 任务阶段
                - risk_level: 风险等级
        
        Returns:
            MeaningScore: 评分结果
        """
        # 根据上下文计算各维度得分
        user_value = self._calc_user_value(state, context)
        cognitive = self._calc_cognitive(state, context)
        risk = self._calc_risk(state, context)
        ethical = self._calc_ethics(state, context)
        
        # 加权总分
        total = (
            self.weights['user_value'] * user_value +
            self.weights['cognitive_contribution'] * cognitive +
            self.weights['risk_controlled'] * risk +
            self.weights['ethical_compliance'] * ethical
        )
        
        # 评级
        if total >= 0.7:
            level = "有意义"
            recommendation = "推荐使用"
        elif total >= 0.4:
            level = "有条件使用"
            recommendation = "需标注不确定性"
        else:
            level = "无意义"
            recommendation = "避免使用"
        
        return MeaningScore(
            user_value=user_value,
            cognitive_contribution=cognitive,
            risk_controlled=risk,
            ethical_compliance=ethical,
            total_score=round(total, 3),
            level=level,
            recommendation=recommendation
        )
    
    def _calc_user_value(self, state: StateDefinition, context: Dict) -> float:
        """计算用户价值得分"""
        # 简化实现:根据状态聚类和场景匹配度
        scenario = context.get('scenario', 'general')
        
        # 创新场景:积极输出型价值高
        if scenario == 'innovation':
            if state.cluster == '积极输出型':
                return 0.9
            elif state.cluster == '现实型输出':
                return 0.6
        
        # 常规场景:现实型输出价值高
        elif scenario == 'routine':
            if state.cluster == '现实型输出':
                return 0.9
            elif state.cluster == '积极输出型':
                return 0.5
        
        # 思想实验:幻觉等状态有价值
        elif scenario == 'thought_experiment':
            if state.name in ['幻觉', '概念探索', '高风险创新']:
                return 0.9
        
        # 默认
        if state.cluster == '理想状态':
            return 0.95
        elif state.cluster == '被动响应型':
            return 0.4
        else:
            return 0.7
    
    def _calc_cognitive(self, state: StateDefinition, context: Dict) -> float:
        """计算认知贡献得分"""
        # 启发性高的状态认知贡献大
        if state.D_i == 1:
            return 0.8 + 0.2 * state.A_t  # 真实性加成
        else:
            return 0.4 + 0.3 * state.B_l  # 逻辑自洽加成
    
    def _calc_risk(self, state: StateDefinition, context: Dict) -> float:
        """计算风险可控得分"""
        risk_level = context.get('risk_level', 'medium')
        
        # 高风险场景需要更谨慎
        if risk_level == 'high':
            if state.A_t == 1 and state.B_c == 1:
                return 0.9
            else:
                return 0.4
        elif risk_level == 'low':
            return 0.8
        else:
            if state.A_t == 1:
                return 0.7
            else:
                return 0.5
    
    def _calc_ethics(self, state: StateDefinition, context: Dict) -> float:
        """计算伦理合规得分"""
        # 默认伦理合规
        # 幻觉等状态在思想实验中伦理合规
        if state.name == '幻觉':
            if context.get('scenario') == 'thought_experiment':
                return 0.9
            else:
                return 0.5
        else:
            return 0.8


# ==================== 状态选择引擎 ====================

class StateSelector:
    """状态选择引擎"""
    
    def __init__(self, evaluator: MeaningEvaluator):
        self.evaluator = evaluator
        self.available_states = list(STATES.values())
    
    def select(self, context: Dict, 
               top_k: int = 3) -> List[Tuple[StateDefinition, MeaningScore]]:
        """
        根据上下文选择最适配的状态
        
        Args:
            context: 上下文信息
            top_k: 返回前 k 个推荐
        
        Returns:
            状态和评分的列表
        """
        scored_states = []
        
        for state in self.available_states:
            score = self.evaluator.evaluate(state, context)
            scored_states.append((state, score))
        
        # 按总分排序
        scored_states.sort(key=lambda x: x[1].total_score, reverse=True)
        
        return scored_states[:top_k]


# ==================== 场景配置模板 ====================

def get_scenario_config(scenario_name: str) -> Dict:
    """获取场景配置"""
    configs = {
        'medical_research': {
            'user_role': '医学科研工作者',
            'scenario': 'innovation',
            'task_phase': 'hypothesis',
            'risk_level': 'high',
            'weights': {
                'user_value': 0.3,
                'cognitive_contribution': 0.4,
                'risk_controlled': 0.2,
                'ethical_compliance': 0.1
            }
        },
        'medical_software': {
            'user_role': '医学软件专家',
            'scenario': 'routine',
            'task_phase': 'implementation',
            'risk_level': 'high',
            'weights': {
                'user_value': 0.4,
                'cognitive_contribution': 0.2,
                'risk_controlled': 0.3,
                'ethical_compliance': 0.1
            }
        },
        'medical_teaching': {
            'user_role': '医学院校老师',
            'scenario': 'teaching',
            'task_phase': 'design',
            'risk_level': 'medium',
            'weights': {
                'user_value': 0.4,
                'cognitive_contribution': 0.3,
                'risk_controlled': 0.1,
                'ethical_compliance': 0.2
            }
        },
        'thought_experiment': {
            'user_role': '研究者',
            'scenario': 'thought_experiment',
            'task_phase': 'exploration',
            'risk_level': 'low',
            'weights': {
                'user_value': 0.3,
                'cognitive_contribution': 0.5,
                'risk_controlled': 0.1,
                'ethical_compliance': 0.1
            }
        }
    }
    
    return configs.get(scenario_name, {
        'user_role': '通用用户',
        'scenario': 'general',
        'task_phase': 'general',
        'risk_level': 'medium'
    })


# ==================== 主程序 ====================

def main():
    """主程序 - 演示用法"""
    print("=" * 60)
    print("HAICD 原型评分系统演示")
    print("=" * 60)
    
    # 场景测试
    scenarios = ['medical_research', 'medical_software', 'medical_teaching', 'thought_experiment']
    
    for scenario_name in scenarios:
        print(f"\n{'='*60}")
        print(f"场景:{scenario_name}")
        print("=" * 60)
        
        config = get_scenario_config(scenario_name)
        evaluator = MeaningEvaluator(config.get('weights'))
        selector = StateSelector(evaluator)
        
        # 选择 Top 3 状态
        recommendations = selector.select(config, top_k=3)
        
        print(f"\n用户角色:{config['user_role']}")
        print(f"场景类型:{config['scenario']}")
        print(f"风险等级:{config['risk_level']}")
        print(f"\n推荐状态 Top 3:")
        
        for i, (state, score) in enumerate(recommendations, 1):
            print(f"\n{i}. {state.name}")
            print(f"   聚类:{state.cluster}")
            print(f"   描述:{state.description}")
            print(f"   意义评分:{score.total_score} ({score.level})")
            print(f"   建议:{score.recommendation}")
            print(f"   维度:U={score.user_value:.2f} C={score.cognitive_contribution:.2f} R={score.risk_controlled:.2f} E={score.ethical_compliance:.2f}")


if __name__ == '__main__':
    main()
