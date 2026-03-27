# HAICD State Engine Scripts

本目录包含 HAICD 状态引擎的核心脚本。

## 脚本清单

| 脚本文件 | 代号 | 功能 | 依赖 |
|---------|------|------|------|
| `haicd_scoring_system.py` | A 脚本 | 状态选择和意义评估 | `pyyaml` |
| `state_flow_tracker.py` | B 脚本 | 状态流跟踪和异常检测 | 无 |
| `haicd_engine.py` | 集成层 | 统一 A/B 脚本，实现历史感知状态选择 | A 脚本，B 脚本 |

## 脚本关系

```
┌─────────────────────────────────────────────────────────┐
│                    HAICD Engine                         │
│                   (haicd_engine.py)                     │
│                                                         │
│  ┌─────────────────┐    ┌─────────────────────────┐   │
│  │  A 脚本          │    │  B 脚本                  │   │
│  │  评分系统        │───▶│  状态流跟踪器            │   │
│  │  - 状态选择      │    │  - 历史记录              │   │
│  │  - 意义评估      │    │  - 动态调整              │   │
│  └─────────────────┘    └─────────────────────────┘   │
│                                                         │
│  核心逻辑：                                             │
│  1. A 提供初始状态推荐                                  │
│  2. B 提供历史状态流                                    │
│  3. 集成层综合两者，动态调整评分                        │
│  4. 每次对话前完成历史综合分析                          │
└─────────────────────────────────────────────────────────┘
```

## 使用方式

### 方式 1：使用集成引擎（推荐）

```python
from haicd_engine import HAICDEngine

# 创建引擎
engine = HAICDEngine(
    session_id="my-session-001",
    scenario="medical_research"
)

# 选择最优状态（结合历史）
context = {
    'user_role': '医学科研工作者',
    'scenario': 'innovation',
    'risk_level': 'high'
}
recommendations = engine.select_state_with_history(context, top_k=3)

# 记录状态
engine.record_and_track(recommendations[0][0].name, context)

# 获取综合分析
analysis = engine.get_comprehensive_analysis()
```

### 方式 2：使用快捷函数

```python
from haicd_engine import select_best_state, track_state

# 选择状态
state_name, score = select_best_state(
    session_id="session-001",
    context={'scenario': 'innovation'},
    scenario='medical_research'
)

# 跟踪状态
report = track_state(
    session_id="session-001",
    state_name=state_name,
    context={'scenario': 'innovation'}
)
```

### 方式 3：单独使用 A 脚本

```python
from haicd_scoring_system import MeaningEvaluator, StateSelector, get_scenario_config

# 加载场景配置
config = get_scenario_config('medical_research')
evaluator = MeaningEvaluator(config.get('weights'))
selector = StateSelector(evaluator)

# 选择状态
context = {'user_role': '医学科研工作者', 'scenario': 'innovation'}
recommendations = selector.select(context, top_k=3)
```

### 方式 4：单独使用 B 脚本

```python
from state_flow_tracker import StateFlowTracker

# 创建跟踪器
tracker = StateFlowTracker("session-001")

# 记录状态
tracker.record_state("顺应", {'scenario': 'medical_research'})

# 获取历史
history = tracker.get_state_history(limit=10)

# 检测异常
anomalies = tracker.detect_anomalies()
```

## 核心逻辑说明

### 历史感知状态选择

集成引擎的核心逻辑遵循以下优先级：

1. **从历史状态流推理**
   - 获取最近 N 次相似场景的状态记录
   - 计算状态分布和一致性得分
   - 识别状态切换模式

2. **从 A 脚本评分系统获取推荐**
   - 基于当前上下文计算各状态的意义评分
   - 考虑场景权重配置

3. **动态调整**
   - 若 A 中找不到 B 所需参数，B 根据人机交互上下文 + LLM 领域知识经验判定
   - 以逻辑/事件/场景一致的相近对话状态为核心依据
   - 推理计算状态流动态赋值

### 调整因子计算

```python
历史调整因子 = 
    频率因子 (0.0 ~ +0.15) +     # 高频状态正向调整
    相似场景因子 (0.0 ~ +0.15) +  # 相似场景中的状态表现
    异常惩罚 (-0.1 ~ 0.0)        # 频繁切换惩罚
```

调整因子范围：**-0.3 ~ +0.3**

### 状态流动态赋值

每次对话开始前：

1. 加载上次及历次对话的状态历史
2. 识别相似场景（场景类型 + 用户角色匹配）
3. 计算状态一致性得分
4. 检测异常（频繁切换、停滞）
5. 基于以上因素调整 A 脚本的原始评分

## 数据存储

状态流数据存储在：
```
~/.openclaw/skills/haicd-state-engine/state_flow.json
```

数据结构：
```json
{
  "sessions": {
    "session-001": {
      "created": "2026-03-27T06:00:00",
      "last_updated": "2026-03-27T06:30:00",
      "current_state": "顺应",
      "states": [
        {
          "state": "顺应",
          "timestamp": "2026-03-27T06:00:00",
          "context": {"scenario": "medical_research"}
        }
      ]
    }
  }
}
```

## 依赖安装

```bash
pip install pyyaml
```

## 测试

```bash
# 测试 A 脚本
python3 haicd_scoring_system.py

# 测试 B 脚本
python3 state_flow_tracker.py

# 测试集成引擎
python3 haicd_engine.py
```

## 版本

- A 脚本：v1.0 (基于 HAICD 理论 02)
- B 脚本：v1.0.0
- 集成引擎：v1.0.0

## 许可

CC BY-NC-SA 4.0

**理论创建者**: Jeason（中国·石家庄）  
**技能实现**: 智联星核 (ZLXH)
