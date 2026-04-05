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
    'user_role': '科研工作者',
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

### 多领域覆盖

HAICD State Engine 支持以下领域的场景配置：

| 领域 | 典型用户 | 关键状态 | 风险特点 |
|------|---------|---------|---------|
| 🏥 健康科学 | 医生、研究员、患者 | 保守型推理、高风险创新 | 患者安全风险高 |
| 🏢 企业管理 | 管理者、HR、员工 | 概念探索、经验驱动型 | 组织稳定性风险 |
| 🏭 工业制造 | 工程师、技术员、工人 | 流程混乱但输出有效、实践验证型 | 生产安全风险 |
| 🌾 农业科技 | 农场主、农技员、经销商 | 资源受限下的灵感激发、保守型推理 | 自然和市场风险 |
| 🔬 科研创新 | 研究员、学者、学生 | 高风险创新、创新性错误、概念探索 | 学术探索风险 |
| 💰 金融服务 | 投资者、分析师、银行员 | 未来导向型输出、资源受限下的保守输出 | 资金安全风险 |
| ⚡ 电力能源 | 工程师、调度员、规划师 | 流程混乱但输出有效、实践验证型 | 公共安全风险 |
| 🎓 教育培训 | 教师、学生、管理者 | 资源受限下的灵感激发、探索性思考 | 教育效果风险 |
| 🚀 科技研发 | 开发者、产品经理、CTO | 理想主义误导、经验驱动型、高风险创新 | 技术失败风险 |

### 详细案例

完整的多领域应用案例见：[HAICD-多领域应用案例.md](docs/HAICD-多领域应用案例.md)，包含：

1. **农业领域案例**：智能农业咨询、病虫害诊断
2. **工业领域案例**：生产线优化、设备故障预测
3. **企业管理案例**：组织变革咨询、战略规划辅助
4. **科研领域案例**：跨学科研究设计、实验失败分析
5. **医疗健康案例**：临床决策支持、健康管理建议
6. **金融服务案例**：投资风险评估、信贷审批辅助
7. **电力能源案例**：电网调度优化、能源转型规划
8. **教育领域案例**：个性化学习路径设计、在线课程质量评估
9. **科技领域案例**：技术选型决策、创新项目管理

每个案例提供：
- 直接LLM泛泛回复 vs HAICD控制后回复对比
- 状态演化过程分析
- 意义评分和验证方法
- 社区用户可自行验证效果

### 预设场景配置

#### 场景 1：学术研究

```yaml
场景：academic_research
用户：科研工作者
推荐状态：高风险创新、未来导向型输出、概念探索
权重配置：
  user_value: 0.3
  cognitive_contribution: 0.4  # 认知贡献优先
  risk_controlled: 0.2
  ethical_compliance: 0.1
```

#### 场景 2：医学软件

```yaml
场景：software_engineering
用户：软件工程专家
推荐状态：顺应、经验驱动型、资源受限下的保守输出
权重配置：
  user_value: 0.4
  cognitive_contribution: 0.2
  risk_controlled: 0.3         # 风险可控优先
  ethical_compliance: 0.1
```

#### 场景 3：思想实验

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

#### 场景 4：农业咨询

```yaml
场景：agricultural_consulting
用户：农场主、农技员
推荐状态：经验驱动型、实践验证型、潜在价值发现
权重配置：
  user_value: 0.4
  cognitive_contribution: 0.3
  risk_controlled: 0.2         # 自然风险控制
  ethical_compliance: 0.1
```

#### 场景 5：工业优化

```yaml
场景：industrial_optimization
用户：生产工程师、维护技术员
推荐状态：流程混乱但输出有效、实践验证型、未来导向型输出
权重配置：
  user_value: 0.5          # 实用价值优先
  cognitive_contribution: 0.2
  risk_controlled: 0.2     # 安全风险控制
  ethical_compliance: 0.1
```

#### 场景 6：金融风控

```yaml
场景：financial_risk_control
用户：投资分析师、信贷审批员
推荐状态：未来导向型输出、资源受限下的保守输出、经验驱动型
权重配置：
  user_value: 0.3
  cognitive_contribution: 0.2
  risk_controlled: 0.4     # 风险控制最高
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

## 🚀 发布到 ClawHub

### 发布准备

1. **GitHub仓库**：技能需要有一个公开的GitHub仓库
2. **ClawHub账号**：使用GitHub账号登录ClawHub
3. **技能元数据**：填写技能信息，包括GitHub仓库链接

### 发布流程

1. 将本技能发布到GitHub（已有仓库：https://github.com/Jeason/haicd-state-engine）
2. 使用GitHub账号登录ClawHub（https://clawhub.ai）
3. 在ClawHub上提交技能，填写GitHub仓库链接
4. 等待审核通过

### 审核要点

- ✅ 理论原创性：HAICD理论由Jeason原创
- ✅ 代码完整性：完整的Python实现和配置
- ✅ 文档完整性：理论文档、使用指南、案例
- ✅ 许可合规：CC BY-NC-SA 4.0非商业许可
- ✅ 实用性验证：多领域案例可验证

### 社区验证

技能发布后，社区用户可：
1. 在不同领域测试HAICD效果
2. 对比直接LLM回复和HAICD控制回复
3. 提供反馈和改进建议
4. 积累各行业最佳实践

## 📬 联系方式

- **GitHub Issues**: https://github.com/Jeason/haicd-state-engine/issues
- **理论创建者**: Jeason（中国·石家庄）
- **技能实现**: 智联星核 (ZLXH)
- **问题反馈**: 通过GitHub Issues或ClawHub评论

---

## 🔄 技能进化路径

### 短期目标（1-3个月）
1. 发布到ClawHub，通过社区审核
2. 收集各领域用户反馈
3. 优化状态选择和权重配置
4. 增加更多行业场景配置

### 中期目标（3-12个月）
1. 建立社区维护机制
2. 开发可视化状态流工具
3. 集成更多AI平台和框架
4. 发表学术论文或技术报告

### 长期目标（1-3年）
1. 成为人机交互标准框架
2. 支持多模态交互情境
3. 建立认证和培训体系
4. 推动行业最佳实践标准化

---

**技能包版本**: v2.0  
**最后更新**: 2026-04-06  
**主要更新**:  
- 新增多领域应用案例（9个领域，18个场景）  
- 完善状态演化分析框架  
- 添加ClawHub发布指南  
- 优化配置模板和文档结构
