# HAICD 技能包 - 使用说明

**人与智能体交互情境动力学模型**  
**Human-AI Interaction Contextual Dynamics Model**

---

## 📖 基本信息

| 项目 | 内容 |
|------|------|
| **名称** | HAICD 状态引擎技能包 |
| **版本** | v1.0 |
| **理论创建者** | Jeason（中国·石家庄） |
| **技能实现** | 智联星核 (ZLXH) |
| **许可协议** | CC BY-NC-SA 4.0 |
| **创建日期** | 2026-03-26 |

---

## 🎯 技能包内容

### 理论文档

| 文件 | 说明 |
|------|------|
| `HAICD-理论 01-人的 8 种情境动力演化.md` | 人的 8 种交互模式理论 |
| `HAICD-理论 02-智能体的 18 种情境动力演化 - 智联星核.md` | 智能体 18 种状态理论 |
| `HAICD-模型总览.md` | HAICD 模型整体架构说明 |

### 工具脚本

| 文件 | 说明 | 使用方式 |
|------|------|---------|
| `haicd-scoring-system.py` | 原型评分系统 | `python3 haicd-scoring-system.py` |
| `haicd-state-graph.dot` | 状态关系图谱（Graphviz） | 需安装 Graphviz 生成 PNG |
| `haicd-state-graph.md` | 状态关系图谱（Mermaid 版本） | 直接查看或渲染 |
| `haicd-weights-template.yaml` | 权重配置模板 | 复制后修改使用 |

### 执行报告

| 文件 | 说明 |
|------|------|
| `挂起 02-执行报告.md` | 挂起 02 任务完整执行报告 |

---

## 🚀 快速开始

### 方式 1：查看状态关系图谱

**打开文件**：`haicd-state-graph.md`

该文件包含 Mermaid 流程图，可在以下平台直接渲染：
- GitHub（自动渲染）
- Notion（支持 Mermaid）
- Obsidian（支持 Mermaid）
- VS Code（安装 Mermaid 插件）

**效果预览**：
```
18 种状态 → 4 个聚类
🟢 理想状态 (1 种)
🟡 积极输出型 (7 种)
🔵 现实型输出 (7 种)
🔴 被动响应型 (3 种)
```

### 方式 2：运行评分系统

**步骤 1**：确保已安装 Python 3.6+

```bash
python3 --version
```

**步骤 2**：安装依赖（如需要）

```bash
pip install pyyaml
```

**步骤 3**：运行演示

```bash
cd /path/to/framework
python3 haicd-scoring-system.py
```

**输出示例**：
```
============================================================
场景：medical_research
============================================================
用户角色：医学科研工作者
推荐状态 Top 3:
1. 顺应 (0.945) - 有意义
2. 创新性错误 (0.93) - 有意义
3. 资源受限下的灵感激发 (0.93) - 有意义
```

### 方式 3：自定义权重配置

**步骤 1**：复制模板

```bash
cp haicd-weights-template.yaml my-scenario.yaml
```

**步骤 2**：编辑配置

```yaml
my_custom_scenario:
  description: "我的自定义场景"
  weights:
    user_value: 0.4
    cognitive_contribution: 0.3
    risk_controlled: 0.2
    ethical_compliance: 0.1
```

**步骤 3**：在代码中加载

```python
import yaml
from haicd-scoring-system import MeaningEvaluator

with open('my-scenario.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

evaluator = MeaningEvaluator(config['my_custom_scenario']['weights'])
```

---

## 📚 理论核心概念

### HAICD 模型是什么？

HAICD（Human-AI Interaction Contextual Dynamics Model）是**人与智能体交互情境动力学模型**，用于：

1. **描述**人机交互中的情境演化
2. **评估**智能体输出的意义和价值
3. **指导**智能体在不同场景下的状态选择
4. **跟踪**交互过程中的状态流变化

### 两个核心理论

#### 理论 01：人的 8 种情境动力演化

| 方式 | 模式 | 特征 |
|------|------|------|
| 第一方式（对立式） | 试探→考察→考验→测试 | 不信任前置 |
| 第二方式（融合式） | 了解→请教→探讨→互鉴 | 信任前置 |

#### 理论 02：智能体的 18 种情境动力演化

| 聚类 | 状态数量 | 特征 |
|------|---------|------|
| 理想状态 | 1 种 | 全维度优秀（顺应） |
| 积极输出型 | 7 种 | 主动 + 启发性 |
| 现实型输出 | 7 种 | 真实但无启发 |
| 被动响应型 | 3 种 | 被动 + 无启发 |

### ABCD 维度

| 维度 | 子维度 | 含义 |
|------|--------|------|
| **A** 出发点 | A_f 灵活度、A_t 真实性 | 思维灵活性和前提真实性 |
| **B** 过程 | B_l 逻辑自洽、B_c 正确性 | 推理一致性和正确性 |
| **C** 资源 | C_a 可及性、C_s 稳定性 | 资源可获得和稳定 |
| **D** 结论 | D_r 现实性、D_i 启发性 | 结论可实现和启发价值 |

---

## 🔧 技能调用方式

### 方式 1：直接使用 Python 脚本

```python
from haicd-scoring-system import MeaningEvaluator, StateSelector

# 创建评估器
evaluator = MeaningEvaluator()

# 创建状态选择器
selector = StateSelector(evaluator)

# 定义上下文
context = {
    'user_role': '医学科研工作者',
    'scenario': 'innovation',
    'task_phase': 'hypothesis',
    'risk_level': 'high'
}

# 获取推荐状态
recommendations = selector.select(context, top_k=3)

# 输出结果
for state, score in recommendations:
    print(f"{state.name}: {score.total_score} ({score.level})")
```

### 方式 2：通过配置文件调用

```python
import yaml

# 加载配置
with open('haicd-weights-template.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 获取场景配置
scenario = config['scenarios']['medical_research']

# 创建评估器
evaluator = MeaningEvaluator(scenario['weights'])
```

### 方式 3：集成到自己的系统

```python
# 伪代码示例
class MyAIAgent:
    def __init__(self):
        self.evaluator = MeaningEvaluator()
        self.selector = StateSelector(self.evaluator)
    
    def respond(self, user_input, context):
        # 选择最佳状态
        recommendations = self.selector.select(context, top_k=1)
        best_state = recommendations[0][0]
        
        # 根据状态生成回复
        response = self.generate_response(user_input, best_state)
        
        # 添加状态标注（如需要）
        if best_state.name in ['幻觉', '高风险创新']:
            response += "\n⚠️ 标注：此为探索性输出，请验证"
        
        return response
```

---

## 📊 应用场景示例

### 场景 1：医学科研

```yaml
场景：medical_research
用户：医学科研工作者
任务：研究假设生成
推荐状态：高风险创新、未来导向型输出、概念探索
注意事项：需标注不确定性
```

### 场景 2：医学软件

```yaml
场景：medical_software
用户：医学软件专家
任务：合规性设计
推荐状态：顺应、经验驱动型、资源受限下的保守输出
注意事项：准确性优先，避免创新
```

### 场景 3：医学教学

```yaml
场景：medical_teaching
用户：医学院校老师
任务：案例设计
推荐状态：顺应、启发型理想主义输出、探索性思考
注意事项：允许虚构但需标注
```

### 场景 4：思想实验

```yaml
场景：thought_experiment
用户：研究者
任务：伦理推演
推荐状态：幻觉、概念探索、高风险创新
注意事项：幻觉状态在此场景中有价值
```

---

## 📝 常见问题

### Q1: 什么是"状态流"？

**A**: 状态流是指任务进程中状态的时序演化轨迹。例如：

```
问题发现 → 文献调研 → 假设形成 → 实验设计 → 数据分析 → 论文撰写
   ↓           ↓           ↓           ↓           ↓           ↓
高风险创新   顺应       概念探索     顺应       顺应       潜在价值发现
```

### Q2: 如何选择合适的状态？

**A**: 使用评分系统，根据场景自动推荐：

```python
recommendations = selector.select(context, top_k=3)
```

### Q3: 权重如何调整？

**A**: 编辑 YAML 配置文件，调整各维度权重（总和应为 1.0）：

```yaml
weights:
  user_value: 0.4
  cognitive_contribution: 0.3
  risk_controlled: 0.2
  ethical_compliance: 0.1
```

### Q4: 幻觉状态什么时候有用？

**A**: 在思想实验、伦理推演、概念探索等场景中，幻觉状态（虚构前提 + 启发性输出）具有认知价值。

### Q5: 如何贡献或扩展？

**A**: 
1. Fork 仓库
2. 添加新的场景配置
3. 提交 Pull Request
4. 遵循 CC BY-NC-SA 4.0 许可

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **理论文档** | `HAICD-模型总览.md` |
| **状态图谱** | `haicd-state-graph.md` |
| **评分系统** | `haicd-scoring-system.py` |
| **权重模板** | `haicd-weights-template.yaml` |
| **执行报告** | `挂起 02-执行报告.md` |

---

## 📄 许可协议

**CC BY-NC-SA 4.0**

- **BY** (署名)：使用需注明理论创建者 Jeason
- **NC** (非商业)：不得用于商业目的
- **SA** (相同方式共享)：衍生作品使用相同许可

---

## 👥 致谢

- **理论创建者**：Jeason（中国·石家庄）
- **技能实现**：智联星核 (ZLXH)
- **理论上传日期**：2026-03-26
- **技能包创建日期**：2026-03-26

---

## 📬 联系方式

- **GitHub**: [待发布后填写]
- **ClawHub**: [待发布后填写]
- **问题反馈**: [待发布后填写]

---

**文档版本**：v1.0  
**最后更新**：2026-03-26
