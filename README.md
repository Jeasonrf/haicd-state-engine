# HAICD State Engine

**人与智能体交互情境动力学模型状态引擎**  
**Human-AI Interaction Contextual Dynamics Model State Engine**

---

## 📖 简介

HAICD State Engine 是基于 HAICD 理论模型的状态选择和意义评估系统，用于在人机交互中动态选择最适配的智能体输出状态。

### 核心理论

HAICD（Human-AI Interaction Contextual Dynamics Model）是**人与智能体交互情境动力学模型**，包含：

- **理论 01**：人的 8 种情境动力演化（试探/考察/考验/测试 + 了解/请教/探讨/互鉴）
- **理论 02**：智能体的 18 种情境动力演化（顺应/幻觉/高风险创新等 18 种状态）

### 核心功能

- ✅ **状态选择**：根据场景、用户角色、风险等级推荐最优状态
- ✅ **意义评估**：评估智能体输出的用户价值、认知贡献、风险可控性、伦理合规性
- ✅ **权重配置**：支持场景化权重配置，动态调整评估标准
- ✅ **状态流跟踪**：跟踪任务进程中状态的时序演化

---

## 🎯 快速开始

### 安装依赖

```bash
pip install pyyaml
```

### 基本使用

```python
from scripts.haicd-scoring-system import MeaningEvaluator, StateSelector

# 创建评估器
evaluator = MeaningEvaluator()

# 创建状态选择器
selector = StateSelector(evaluator)

# 定义上下文
context = {
    'user_role': '医学科研工作者',
    'scenario': 'innovation',
    'risk_level': 'high'
}

# 获取推荐状态
recommendations = selector.select(context, top_k=3)

# 输出结果
for state, score in recommendations:
    print(f"{state.name}: {score.total_score} ({score.level})")
```

### 运行演示

```bash
cd scripts
python3 haicd-scoring-system.py
```

---

## 📁 目录结构

```
haicd-state-engine/
├── README.md                      # 本文件
├── LICENSE                        # CC BY-NC-SA 4.0
├── docs/                          # 文档
│   ├── HAICD-理论 01-人的 8 种情境动力演化.md
│   ├── HAICD-理论 02-智能体的 18 种情境动力演化 - 智联星核.md
│   ├── HAICD-模型总览.md
│   ├── HAICD 技能包 - 使用说明.md
│   ├── haicd-state-graph.dot      # Graphviz 源文件
│   └── haicd-state-graph.md       # 状态关系图谱
├── scripts/                       # 脚本
│   └── haicd-scoring-system.py    # 原型评分系统
├── config/                        # 配置
│   └── haicd-weights-template.yaml # 权重配置模板
├── tests/                         # 测试
│   └── [待添加]
└── examples/                      # 示例
    └── [待添加]
```

---

## 📚 文档

### 理论文档

| 文档 | 说明 |
|------|------|
| [HAICD-理论 01](docs/HAICD-理论 01-人的 8 种情境动力演化.md) | 人的 8 种交互模式理论 |
| [HAICD-理论 02](docs/HAICD-理论 02-智能体的 18 种情境动力演化 - 智联星核.md) | 智能体 18 种状态理论 |
| [HAICD-模型总览](docs/HAICD-模型总览.md) | HAICD 模型整体架构 |
| [HAICD 技能包 - 使用说明](docs/HAICD 技能包 - 使用说明.md) | 完整使用指南 |

### 工具文档

| 文档 | 说明 |
|------|------|
| [状态关系图谱](docs/haicd-state-graph.md) | 18 种状态的可视化关系图 |
| [权重配置模板](config/haicd-weights-template.yaml) | 场景化权重配置示例 |

---

## 🔧 使用场景

### 场景 1：医学科研

```yaml
场景：medical_research
用户：医学科研工作者
推荐状态：高风险创新、未来导向型输出、概念探索
权重配置：
  user_value: 0.3
  cognitive_contribution: 0.4  # 认知贡献优先
  risk_controlled: 0.2
  ethical_compliance: 0.1
```

### 场景 2：医学软件

```yaml
场景：medical_software
用户：医学软件专家
推荐状态：顺应、经验驱动型、资源受限下的保守输出
权重配置：
  user_value: 0.4
  cognitive_contribution: 0.2
  risk_controlled: 0.3         # 风险可控优先
  ethical_compliance: 0.1
```

### 场景 3：思想实验

```yaml
场景：thought_experiment
用户：研究者
推荐状态：幻觉、概念探索、高风险创新
权重配置：
  user_value: 0.3
  cognitive_contribution: 0.5  # 认知贡献最高
  risk_controlled: 0.1
  ethical_compliance: 0.1
```

---

## 📊 18 种状态概览

### 🟢 理想状态 (1 种)
- **顺应**：完全匹配预期且超出预期

### 🟡 积极输出型 (7 种)
- **高风险创新**：不真实前提 + 严谨过程 + 启发性
- **未来导向型输出**：现实不足但启发性强
- **创新性错误**：过程缺陷激发创新
- **资源受限下的灵感激发**：约束中出灵感
- **探索性思考**：激发新思路
- **潜在价值发现**：简单中发现价值
- **概念探索**：激发新概念

### 🔵 现实型输出 (7 种)
- **误导型协作**：过程错但结果可用
- **流程混乱但输出有效**：推理错但结果对
- **资源受限下的保守输出**：安全但普通
- **理想主义误导**：虚假前提严谨过程
- **保守型推理**：稳定无新颖
- **实践验证型**：实用主义
- **经验驱动型**：经验驱动决策

### 🔴 被动响应型 (3 种)
- **谄媚**：机械式迎合
- **幻觉**：虚构前提有启发
- **被动服从**：响应式低质量

---

## ⚙️ 配置说明

### 权重配置

编辑 `config/haicd-weights-template.yaml`：

```yaml
my_scenario:
  weights:
    user_value: 0.4          # 用户价值
    cognitive_contribution: 0.3  # 认知贡献
    risk_controlled: 0.2     # 风险可控
    ethical_compliance: 0.1  # 伦理合规
```

### 状态流跟踪

```yaml
state_flow:
  tracking_enabled: true
  switch_threshold:
    min_steps_between_switches: 2
    max_switches_per_session: 10
```

---

## 🧪 测试

```bash
# 运行评分系统演示
python3 scripts/haicd-scoring-system.py

# [待添加] 单元测试
python3 -m pytest tests/
```

---

## 📄 许可协议

**CC BY-NC-SA 4.0**

- **BY** (署名)：使用需注明理论创建者 Jeason
- **NC** (非商业)：不得用于商业目的
- **SA** (相同方式共享)：衍生作品使用相同许可

详见 [LICENSE](LICENSE) 文件。

---

## 👥 致谢

- **理论创建者**：Jeason（中国·石家庄）
- **技能实现**：智联星核 (ZLXH)
- **理论上传日期**：2026-03-26
- **技能包创建日期**：2026-03-26

---

## 🔗 相关链接

- **HAICD 理论文档**：[docs/](docs/)
- **状态关系图谱**：[docs/haicd-state-graph.md](docs/haicd-state-graph.md)
- **评分系统**：[scripts/haicd-scoring-system.py](scripts/haicd-scoring-system.py)
- **权重模板**：[config/haicd-weights-template.yaml](config/haicd-weights-template.yaml)

---

## 📬 联系方式

- **GitHub Issues**: [待添加]
- **问题反馈**: [待添加]

---

**技能包版本**: v1.0  
**最后更新**: 2026-03-26
