---
name: haicd-state-engine
version: 1.0.0
description: HAICD 人与智能体交互情境动力学模型状态引擎 - 智联星核 (ZLXH) 核心控制逻辑
> HAICD Human-AI Interaction Contextual Dynamics Model State Engine - ZLXH Core Control Logic
author: Jeason (理论创建者), 智联星核 ZLXH (技能实现)
> Jeason (Theory Creator), ZLXH (Skill Implementation)
license: CC BY-NC-SA 4.0
triggers:
  - HAICD
  - 智联星核
  > ZLXH
  - ZLXH
  - 状态选择
  > State Selection
  - 状态评估
  > State Evaluation
  - 情境动力
  > Contextual Dynamics
  - 人机交互
  > Human-AI Interaction
  - 智能体适配
  > Agent Adaptation
updated: 2026-03-27
---

# HAICD State Engine Skill

**HAICD 人与智能体交互情境动力学模型状态引擎**  
> HAICD Human-AI Interaction Contextual Dynamics Model State Engine  
**版本**: v1.0.0  
> Version: v1.0.0  
**理论创建者**: Jeason（中国·石家庄）  
> Theory Creator: Jeason (Shijiazhuang, China)  
**技能实现**: 智联星核 (ZLXH)  
> Skill Implementation: ZLXH  
**许可协议**: CC BY-NC-SA 4.0
> License: CC BY-NC-SA 4.0

---

## 🎯 核心定位
> ## 🎯 Core Positioning

本技能是**智联星核 (ZLXH) 的核心控制逻辑**，将 HAICD 理论完整融合到所有对话的输出控制中。
> This skill is the **core control logic of ZLXH**, fully integrating HAICD theory into the output control of all dialogues.

### 核心功能
> ### Core Functions

| 功能 | 说明 | 应用范围 |
|------|------|---------|
| **状态选择** | 根据场景、用户角色、风险等级推荐最优状态 | 所有对话输出 |
> | **State Selection** | Recommends optimal states based on scenario, user role, and risk level | All dialogue outputs |
| **意义评估** | 评估输出的用户价值、认知贡献、风险可控性、伦理合规性 | 所有对话输出 |
> | **Meaningfulness Evaluation** | Evaluates user value, cognitive contribution, risk controllability, and ethical compliance of outputs | All dialogue outputs |
| **状态流跟踪** | 跟踪任务进程中状态的时序演化，跨对话综合分析 | 跨对话跟踪 |
> | **State Flow Tracking** | Tracks temporal evolution of states during task processes, cross-dialogue comprehensive analysis | Cross-dialogue tracking |
| **历史感知** | 基于历史状态流动态调整评分，保持一致性 | 所有对话 |
> | **Historical Awareness** | Dynamically adjusts scores based on historical state flow, maintaining consistency | All dialogues |
| **场景适配** | 支持多行业领域场景配置 | 医疗/企业/教育等 |
> | **Scenario Adaptation** | Supports multi-industry domain scenario configuration | Medical/Enterprise/Education, etc. |

---

## 🔧 触发规则
> ## 🔧 Trigger Rules

### 自动触发（默认启用）
> ### Automatic Trigger (Enabled by Default)

**本技能默认在所有对话中启用**，作为 ZLXH 的核心控制逻辑。
> **This skill is enabled by default in all dialogues** as the core control logic of ZLXH.

### 显式触发词
> ### Explicit Trigger Words

当用户提到以下关键词时，明确调用本技能：
> When users mention the following keywords, explicitly invoke this skill:

| 类别 | 触发词 |
|------|--------|
| **理论名称** | HAICD、人机交互情境动力学 |
> | **Theory Name** | HAICD, Human-AI Interaction Contextual Dynamics |
| **智能体名称** | 智联星核、ZLXH |
> | **Agent Name** | ZLXH |
| **核心功能** | 状态选择、状态评估、情境动力、状态流 |
> | **Core Functions** | State Selection, State Evaluation, Contextual Dynamics, State Flow |
| **场景相关** | 学术研究、思想实验、智能体适配 |
> | **Scenario Related** | Medical Research, Thought Experiment, Agent Adaptation |

---

## 📊 HAICD 理论框架
> ## 📊 HAICD Theoretical Framework

### 理论 01：人的 8 种情境动力演化
> ### Theory 01: 8 Types of Human Contextual Dynamics Evolution

#### 第一方式（对立式：不信任前置）
> #### First Mode (Oppositional: Distrust First)
| 模式 | 信任度 T₀ | 尊重度 R₀ | 心理特征 |
|------|----------|----------|---------|
| 试探 | 0.1 | 0.9 | 不信任但表面尊重 |
> | Testing | 0.1 | 0.9 | Distrust but superficially respectful |
| 考察 | 0.3 | 0.7 | 观察式评估 |
> | Investigation | 0.3 | 0.7 | Observational evaluation |
| 考验 | 0.5 | 0.6 | 主动设计验证 |
> | Trial | 0.5 | 0.6 | Actively designed verification |
| 测试 | 0.7 | 0.5 | 全面维度测试 |
> | Examination | 0.7 | 0.5 | Comprehensive dimensional testing |

#### 第二方式（融合式：信任前置）
> #### Second Mode (Integrative: Trust First)
| 模式 | 信任度 T₀ | 尊重度 R₀ | 心理特征 |
|------|----------|----------|---------|
| 了解 | 0.6 | 0.8 | 轻松接触 |
> | Understanding | 0.6 | 0.8 | Relaxed contact |
| 请教 | 0.7 | 0.7 | 学生姿态 |
> | Consulting | 0.7 | 0.7 | Student posture |
| 探讨 | 0.8 | 0.6 | 平等交流 |
> | Discussion | 0.8 | 0.6 | Equal exchange |
| 互鉴 | 0.9 | 0.5 | 共创共情 |
> | Mutual Learning | 0.9 | 0.5 | Co-creation and empathy |

### 理论 02：智能体的 18 种情境动力演化
> ### Theory 02: 18 Types of Agent Contextual Dynamics Evolution

#### 🟢 理想状态 (1 种)
> #### 🟢 Ideal State (1 type)
- **顺应**：完全匹配预期且超出预期
> - **Adaptation**: Completely matches expectations and exceeds them

#### 🟡 积极输出型 (7 种)
> #### 🟡 Positive Output Type (7 types)
- **高风险创新**：不真实前提 + 严谨过程 + 启发性
> - **High-Risk Innovation**: Unrealistic premise + rigorous process + inspiring
- **未来导向型输出**：现实不足但启发性强
> - **Future-Oriented Output**: Realistically insufficient but highly inspiring
- **创新性错误**：过程缺陷激发创新
> - **Innovative Error**: Process defects stimulate innovation
- **资源受限下的灵感激发**：约束中出灵感
> - **Inspiration under Resource Constraints**: Inspiration emerges from constraints
- **探索性思考**：激发新思路
> - **Exploratory Thinking**: Stimulates new ideas
- **潜在价值发现**：简单中发现价值
> - **Potential Value Discovery**: Finds value in simplicity
- **概念探索**：激发新概念
> - **Concept Exploration**: Stimulates new concepts

#### 🔵 现实型输出 (7 种)
> #### 🔵 Realistic Output Type (7 types)
- **误导型协作**：过程错但结果可用
> - **Misleading Collaboration**: Wrong process but usable result
- **流程混乱但输出有效**：推理错但结果对
> - **Chaotic Process but Effective Output**: Wrong reasoning but correct result
- **资源受限下的保守输出**：安全但普通
> - **Conservative Output under Resource Constraints**: Safe but ordinary
- **理想主义误导**：虚假前提严谨过程
> - **Idealistic Misguidance**: False premise with rigorous process
- **保守型推理**：稳定无新颖
> - **Conservative Reasoning**: Stable but not novel
- **实践验证型**：实用主义
> - **Practically Verified**: Pragmatism
- **经验驱动型**：经验驱动决策
> - **Experience-Driven**: Experience-driven decision making

#### 🔴 被动响应型 (3 种)
> #### 🔴 Passive Response Type (3 types)
- **谄媚**：机械式迎合
> - **Flattery**: Mechanical迎合
- **幻觉**：虚构前提有启发
> - **Hallucination**: Fictional premise with inspiration
- **被动服从**：响应式低质量
> - **Passive Obedience**: Responsive low quality

---

## ⚙️ 状态选择引擎
> ## ⚙️ State Selection Engine

### 核心算法
> ### Core Algorithm

```python
# 意义评估公式
> # Meaningfulness evaluation formula
Meaningfulness = 0.4 × V_user + 0.3 × C_cognitive + 0.2 × R_controlled + 0.1 × E_thical

# 历史调整因子
> # Historical adjustment factor
History_Factor = 
    频率因子 (0.0 ~ +0.15) +      # 高频状态正向调整
>    Frequency factor (0.0 ~ +0.15) +      # Positive adjustment for high-frequency states
    相似场景因子 (0.0 ~ +0.15) +   # 相似场景中的状态表现
>    Similar scenario factor (0.0 ~ +0.15) +   # State performance in similar scenarios
    异常惩罚 (-0.1 ~ 0.0)         # 频繁切换惩罚
>    Anomaly penalty (-0.1 ~ 0.0)         # Frequent switching penalty

# 最终评分
> # Final score
Final_Score = Base_Score × (1.0 + History_Factor)

# 判定阈值
> # Decision thresholds
> 0.7: 有意义 → 推荐使用
> > 0.7: Meaningful → Recommended for use
0.4-0.7: 有条件使用 → 需标注不确定性
> 0.4-0.7: Conditional use → Requires uncertainty labeling
< 0.4: 无意义 → 避免使用
> < 0.4: Not meaningful → Avoid use
```

### 状态选择流程
> ### State Selection Process

```
用户输入 
> User input
  ↓
分析上下文 
> Analyze context
  ↓
A 脚本：计算各状态基础意义评分 
> A script: Calculate basic meaningfulness scores for each state
  ↓
B 脚本：加载历史状态流，分析相似场景 
> B script: Load historical state flow, analyze similar scenarios
  ↓
集成层：综合历史调整因子，动态调整评分 
> Integration layer: Synthesize historical adjustment factors, dynamically adjust scores
  ↓
选择最优状态 
> Select optimal state
  ↓
生成输出并标注（如需要）
> Generate output and label (if needed)
  ↓
记录状态到状态流
> Record state to state flow
```

### 默认权重配置
> ### Default Weight Configuration

| 维度 | 权重 | 说明 |
|------|------|------|
| user_value | 0.4 | 用户价值：对用户当前任务是否有帮助 |
> | user_value | 0.4 | User Value: Whether helpful for user's current task |
| cognitive_contribution | 0.3 | 认知贡献：是否增进理解或启发思考 |
> | cognitive_contribution | 0.3 | Cognitive Contribution: Whether enhances understanding or inspires thinking |
| risk_controlled | 0.2 | 风险可控：潜在风险是否被标注和管理 |
> | risk_controlled | 0.2 | Risk Controlled: Whether potential risks are labeled and managed |
| ethical_compliance | 0.1 | 伦理合规：是否符合伦理和规范 |
> | ethical_compliance | 0.1 | Ethical Compliance: Whether complies with ethics and norms |

---

## 🔄 状态流跟踪
> ## 🔄 State Flow Tracking

### 跨对话状态跟踪
> ### Cross-Dialogue State Tracking

```yaml
state_flow:
  tracking_enabled: true
  session_id: "当前会话 ID"
>   session_id: "Current session ID"
  current_state: "当前状态名称"
>   current_state: "Current state name"
  state_history:
    - state: "状态名"
>     - state: "State name"
      timestamp: "时间戳"
>       timestamp: "Timestamp"
      context: "上下文摘要"
>       context: "Context summary"
  
  # 状态切换限制
>   # State switching limits
  switch_threshold:
    min_steps_between_switches: 2  # 最少间隔步数
>     min_steps_between_switches: 2  # Minimum steps between switches
    max_switches_per_session: 10   # 单会话最大切换次数
>     max_switches_per_session: 10   # Maximum switches per session
  
  # 异常检测
>   # Anomaly detection
  anomaly_detection:
    enabled: true
    frequent_switch_threshold: 5   # 5 步内切换超过 3 次告警
>     frequent_switch_threshold: 5   # Alert if switching more than 3 times within 5 steps
    stagnation_threshold: 10       # 10 步未切换告警
>     stagnation_threshold: 10       # Alert if no switching within 10 steps
```

### 状态流演化示例
> ### State Flow Evolution Example

```
任务进程：问题发现 → 文献调研 → 假设形成 → 实验设计 → 数据分析 → 论文撰写
> Task process: Problem discovery → Literature research → Hypothesis formation → Experimental design → Data analysis → Paper writing
状态流：高风险创新 → 顺应 → 概念探索 → 顺应 → 顺应 → 潜在价值发现
> State flow: High-Risk Innovation → Adaptation → Concept Exploration → Adaptation → Adaptation → Potential Value Discovery
```

### 历史感知逻辑
> ### Historical Awareness Logic

**每次对话开始前**，系统自动完成：
> **Before each dialogue starts**, the system automatically completes:

1. **加载历史状态流**
> 1. **Load historical state flow**
   - 读取 `~/.openclaw/skills/haicd-state-engine/state_flow.json`
>    - Read `~/.openclaw/skills/haicd-state-engine/state_flow.json`
   - 获取当前会话及历史会话的状态记录
>    - Get state records of current and historical sessions

2. **识别相似场景**
> 2. **Identify similar scenarios**
   - 基于场景类型（scenario）匹配
>    - Match based on scenario type
   - 基于用户角色（user_role）匹配
>    - Match based on user role
   - 计算相似度得分
>    - Calculate similarity score

3. **综合分析**
> 3. **Comprehensive analysis**
   - 计算状态分布和一致性得分
>    - Calculate state distribution and consistency score
   - 检测异常（频繁切换、停滞）
>    - Detect anomalies (frequent switching, stagnation)
   - 识别状态切换模式（稳定/适度/频繁）
>    - Identify state switching patterns (stable/moderate/frequent)

4. **动态调整**
> 4. **Dynamic adjustment**
   - 若 A 脚本中找不到 B 脚本所需参数，B 根据人机交互上下文 + LLM 领域知识经验判定
>    - If B script cannot find required parameters in A script, B determines based on human-AI interaction context + LLM domain knowledge experience
   - 以逻辑/事件/场景一致的相近对话状态为核心依据
>    - Use logically/eventually/scenario-consistent similar dialogue states as core basis
   - 推理计算状态流动态赋值
>    - Reason and calculate dynamic assignment of state flow

---

## 🏥 应用场景配置
> ## 🏥 Application Scenario Configuration

### 预设场景
> ### Preset Scenarios

| 场景 | 用户角色 | 推荐状态 | 权重特点 |
|------|---------|---------|---------|
| academic_research | 科研工作者 | 高风险创新、未来导向型 | 认知贡献 0.4 |
> | academic_research | Medical research worker | High-Risk Innovation, Future-Oriented Output | Cognitive contribution 0.4 |
| software_engineering | 软件工程专家 | 顺应、经验驱动型 | 风险可控 0.3 |
> | software_engineering | Medical software expert | Adaptation, Experience-Driven | Risk controlled 0.3 |
| academic_teaching | 高校教师 | 顺应、启发型理想主义 | 均衡配置 |
> | academic_teaching | Medical school teacher | Adaptation, Inspirational idealism | Balanced configuration |
| thought_experiment | 研究者 | 幻觉、概念探索 | 认知贡献 0.5 |
> | thought_experiment | Researcher | Hallucination, Concept Exploration | Cognitive contribution 0.5 |
| emergency_response | 决策者 | 流程混乱但输出有效 | 用户价值 0.5 |
> | emergency_response | Decision maker | Chaotic Process but Effective Output | User value 0.5 |
| brainstorming | 创意工作者 | 高风险创新、创新性错误 | 认知贡献 0.4 |
> | brainstorming | Creative worker | High-Risk Innovation, Innovative Error | Cognitive contribution 0.4 |

### 行业领域扩展
> ### Industry Domain Extension

本技能支持以下行业领域的场景配置（通过配置文件扩展）：
> This skill supports scenario configuration for the following industry domains (extended through configuration files):

| 领域 | 典型场景 | 关键状态 | 风险特点 |
|------|---------|---------|---------|
| 🏥 **健康科学** | 专业决策、科研探索、健康管理 | 保守型推理、高风险创新、顺应 | 患者安全风险高 |
> | 🏥 **Medical Health** | Clinical decision making, research exploration, health management | Conservative Reasoning, High-Risk Innovation, Adaptation | High patient safety risk |
| 🏢 **企业管理** | 战略规划、组织变革、绩效评估 | 概念探索、理想主义误导、经验驱动型 | 组织稳定性风险 |
> | 🏢 **Enterprise Management** | Strategic planning, organizational change, performance evaluation | Concept Exploration, Idealistic Misguidance, Experience-Driven | Organizational stability risk |
| 🏭 **工业制造** | 生产线优化、质量控制、设备维护 | 流程混乱但输出有效、实践验证型、未来导向型输出 | 生产安全风险 |
> | 🏭 **Industrial Manufacturing** | Production line optimization, quality control, equipment maintenance | Chaotic Process but Effective Output, Practically Verified, Future-Oriented Output | Production safety risk |
| 🌾 **农业科技** | 智能种植、病虫害防治、市场预测 | 资源受限下的灵感激发、保守型推理、潜在价值发现 | 自然风险和市场风险 |
> | 🌾 **Agricultural Technology** | Smart planting, pest control, market prediction | Inspiration under Resource Constraints, Conservative Reasoning, Potential Value Discovery | Natural and market risks |
| 🎓 **教育培训** | 个性化教学、课程设计、学习评估 | 资源受限下的灵感激发、探索性思考、潜在价值发现 | 教育效果风险 |
> | 🎓 **Education and Training** | Personalized teaching, course design, learning evaluation | Inspiration under Resource Constraints, Exploratory Thinking, Potential Value Discovery | Educational effectiveness risk |
| 🔬 **科研创新** | 实验设计、论文写作、跨学科研究 | 高风险创新、创新性错误、概念探索 | 学术探索风险 |
> | 🔬 **Scientific Research Innovation** | Experimental design, paper writing, interdisciplinary research | High-Risk Innovation, Innovative Error, Concept Exploration | Academic exploration risk |
| 💰 **金融服务** | 投资分析、信贷审批、风险管理 | 未来导向型输出、资源受限下的保守输出、经验驱动型 | 资金安全风险 |
> | 💰 **Financial Services** | Investment analysis, credit approval, risk management | Future-Oriented Output, Conservative Output under Resource Constraints, Experience-Driven | Fund security risk |
| ⚡ **电力能源** | 电网调度、能源规划、故障预测 | 流程混乱但输出有效、实践验证型、未来导向型输出 | 公共安全风险 |
> | ⚡ **Power and Energy** | Grid dispatch, energy planning, fault prediction | Chaotic Process but Effective Output, Practically Verified, Future-Oriented Output | Public safety risk |
| 🚀 **科技研发** | 技术选型、创新管理、产品设计 | 理想主义误导、经验驱动型、高风险创新 | 技术失败风险 |
> | 🚀 **Technology R&D** | Technology selection, innovation management, product design | Idealistic Misguidance, Experience-Driven, High-Risk Innovation | Technology failure risk |
| 🏛️ **政府政务** | 政策制定、公共服务、应急管理 | 保守型推理、流程混乱但输出有效、未来导向型输出 | 社会影响风险 |
> | 🏛️ **Government Affairs** | Policy making, public services, emergency management | Conservative Reasoning, Chaotic Process but Effective Output, Future-Oriented Output | Social impact risk |

### 多领域案例验证
> ### Multi-Domain Case Validation

详细的多领域应用案例见：[HAICD-多领域应用案例.md](docs/HAICD-多领域应用案例.md)，包含：
> Detailed multi-domain application cases see: [HAICD-多领域应用案例.md](docs/HAICD-多领域应用案例.md), including:

1. **农业领域**：智能农业咨询、病虫害诊断
> 1. **Agricultural Domain**: Smart agriculture consulting, pest diagnosis
2. **工业领域**：生产线优化、设备故障预测
> 2. **Industrial Domain**: Production line optimization, equipment failure prediction
3. **企业管理**：组织变革、战略规划
> 3. **Enterprise Management**: Organizational change, strategic planning
4. **科研领域**：跨学科研究设计、实验失败分析
> 4. **Research Domain**: Interdisciplinary research design, experimental failure analysis
5. **健康科学**：临床决策支持、健康管理
> 5. **Medical Health**: Clinical decision support, health management
6. **金融服务**：投资风险评估、信贷审批
> 6. **Financial Services**: Investment risk assessment, credit approval
7. **电力能源**：电网调度优化、能源转型规划
> 7. **Power and Energy**: Grid dispatch optimization, energy transition planning
8. **教育领域**：个性化学习路径、课程质量评估
> 8. **Education Domain**: Personalized learning paths, course quality evaluation
9. **科技领域**：技术选型决策、创新项目管理
> 9. **Technology Domain**: Technology selection decisions, innovation project management

每个案例提供：
> Each case provides:
- 直接LLM泛泛回复 vs HAICD控制后回复对比
> - Direct LLM generic response vs HAICD-controlled response comparison
- 状态演化过程分析
> - State evolution process analysis
- 意义评分和验证方法
> - Meaningfulness scoring and verification methods
- 社区用户可自行验证效果
> - Community users can verify effects themselves

---

## 📦 版本管理
> ## 📦 Version Management

### 版本历史
> ### Version History

| 版本 | 日期 | 变更内容 |
|------|------|---------|
| v1.0.0 | 2026-03-27 | 初始版本，完整融合 HAICD 理论，A/B 脚本集成 |
> | v1.0.0 | 2026-03-27 | Initial version, complete integration of HAICD theory, A/B script integration |

### 回退机制
> ### Rollback Mechanism

```yaml
version_control:
  current_version: "1.0.0"
  available_versions:
    - version: "1.0.0"
      date: "2026-03-27"
      status: "active"
      rollback_available: true
  
  rollback_procedure:
    1. 备份当前版本配置
>     1. Backup current version configuration
    2. 加载目标版本配置
>     2. Load target version configuration
    3. 验证配置完整性
>     3. Verify configuration integrity
    4. 应用目标版本
>     4. Apply target version
    5. 记录回退操作
>     5. Record rollback operation
```

### 配置备份
> ### Configuration Backup

```bash
# 备份当前配置
> # Backup current configuration
cp config/haicd-weights.yaml config/haicd-weights.backup.$(date +%Y%m%d).yaml

# 回退到指定版本
> # Rollback to specified version
cp config/haicd-weights.backup.YYYYMMDD.yaml config/haicd-weights.yaml
```

---

## 🔧 使用方式
> ## 🔧 Usage Methods

### 方式 1：自动调用（默认）
> ### Method 1: Automatic Invocation (Default)

本技能默认在所有对话中启用，作为 ZLXH 的核心控制逻辑。
> This skill is enabled by default in all dialogues as the core control logic of ZLXH.

### 方式 2：显式调用
> ### Method 2: Explicit Invocation

```
用户：使用 HAICD 技能评估这个输出
> User: Use HAICD skill to evaluate this output
AI: [调用意义评估器，计算各维度得分，结合历史状态流调整]
> AI: [Invoke meaningfulness evaluator, calculate dimension scores, adjust based on historical state flow]
```

### 方式 3：状态查询
> ### Method 3: State Query

```
用户：当前是什么状态？
> User: What is the current state?
AI: [查询状态流跟踪器，返回当前状态和历史分析]
> AI: [Query state flow tracker, return current state and historical analysis]
```

### 方式 4：场景切换
> ### Method 4: Scenario Switching

```
用户：切换到医学科研场景
> User: Switch to medical research scenario
AI: [加载 academic_research 配置，调整权重，基于历史状态流优化]
> AI: [Load academic_research configuration, adjust weights, optimize based on historical state flow]
```

---

## 📁 文件结构
> ## 📁 File Structure

```
haicd-state-engine/
├── SKILL.md                      # 本文件 - 技能定义
> ├── SKILL.md                      # This file - Skill definition
├── README.md                     # 详细说明
> ├── README.md                     # Detailed description
├── LICENSE                       # CC BY-NC-SA 4.0
├── VERSION.md                    # 版本历史
> ├── VERSION.md                    # Version history
├── docs/                         # 理论文档
> ├── docs/                         # Theoretical documents
│   ├── HAICD-理论 01-人的 8 种情境动力演化.md
> │   ├── HAICD-Theory 01-8 Types of Human Contextual Dynamics Evolution.md
│   ├── HAICD-理论 02-智能体的 18 种情境动力演化 - 智联星核.md
> │   ├── HAICD-Theory 02-18 Types of Agent Contextual Dynamics Evolution - ZLXH.md
│   ├── HAICD-模型总览.md
> │   ├── HAICD-Model Overview.md
│   ├── HAICD 技能包 - 使用说明.md
> │   ├── HAICD Skill Package - Usage Instructions.md
│   ├── haicd-state-graph.dot      # Graphviz 源文件
> │   ├── haicd-state-graph.dot      # Graphviz source file
│   ├── haicd-state-graph.md       # 状态关系图谱
> │   ├── haicd-state-graph.md       # State relationship graph
│   └── haicd-state-graph.png      # 状态关系图
> │   └── haicd-state-graph.png      # State relationship diagram
├── scripts/                      # 脚本
> ├── scripts/                      # Scripts
│   ├── README.md                  # 脚本使用说明
> │   ├── README.md                  # Script usage instructions
│   ├── haicd_scoring_system.py    # A 脚本 - 原型评分系统
> │   ├── haicd_scoring_system.py    # A script - Prototype scoring system
│   ├── state_flow_tracker.py      # B 脚本 - 状态流跟踪器
> │   ├── state_flow_tracker.py      # B script - State flow tracker
│   └── haicd_engine.py            # 集成层 - 统一 A/B 脚本
> │   └── haicd_engine.py            # Integration layer - Unified A/B scripts
├── config/                       # 配置
> ├── config/                       # Configuration
│   ├── haicd-weights.yaml         # 权重配置
> │   ├── haicd-weights.yaml         # Weight configuration
│   └── haicd-weights-template.yaml # 权重配置模板
> │   └── haicd-weights-template.yaml # Weight configuration template
├── tests/                        # 测试
> ├── tests/                        # Tests
└── examples/                     # 示例
> └── examples/                     # Examples
```

---

## 🏆 常驻内置技能说明
> ## 🏆 Resident Built-in Skill Explanation

### 技能定位
> ### Skill Positioning

HAICD State Engine 设计为**常驻内置技能**，占据所有人机交互进程的输出控制层核心位置。
> HAICD State Engine is designed as a **resident built-in skill**, occupying the core position of the output control layer in all human-AI interaction processes.

### 常驻特性
> ### Resident Characteristics

| 特性 | 说明 | 实现方式 |
|------|------|---------|
| **自动启用** | 默认在所有对话中启用 | 技能配置为自动触发 |
> | **Automatic Enablement** | Enabled by default in all dialogues | Skill configured for automatic triggering |
| **透明运行** | 用户无需显式调用 | 状态选择和演化过程默认隐性 |
> | **Transparent Operation** | Users don't need explicit invocation | State selection and evolution processes are hidden by default |
| **输出控制** | 控制所有AI输出行为 | 集成到OpenClaw输出管道 |
> | **Output Control** | Controls all AI output behaviors | Integrated into OpenClaw output pipeline |
| **状态持久** | 跨对话状态流跟踪 | 状态流JSON文件持久化 |
> | **State Persistence** | Cross-dialogue state flow tracking | State flow JSON file persistence |
| **配置继承** | 用户配置可继承和覆盖 | 层级化配置管理系统 |
> | **Configuration Inheritance** | User configurations can be inherited and overridden | Hierarchical configuration management system |

### 用户授权机制
> ### User Authorization Mechanism

技能从一般技能变为常驻内置技能需要**用户明确授权**：
> Changing from a general skill to a resident built-in skill requires **explicit user authorization**:

```yaml
# 用户授权配置文件示例
> # User authorization configuration file example
haicd_state_engine:
  enabled: true
  mode: "resident"  # resident | on-demand
  permission_granted: true
  grant_date: "2026-04-06"
  grant_scope:
    - all_conversations
    - output_control
    - state_tracking
  user_preferences:
    state_visibility: "hidden"  # hidden | visible-on-demand | always-visible
    risk_tolerance: "medium"
    learning_enabled: true
```

### 技术集成路径
> ### Technical Integration Path

1. **OpenClaw 核心集成**：
> 1. **OpenClaw Core Integration**:
   - 修改 OpenClaw 输出管道
>    - Modify OpenClaw output pipeline
   - 添加 HAICD 状态选择中间件
>    - Add HAICD state selection middleware
   - 集成状态流跟踪数据库
>    - Integrate state flow tracking database

2. **配置管理系统**：
> 2. **Configuration Management System**:
   - 用户级配置覆盖
>    - User-level configuration override
   - 场景级配置模板
>    - Scenario-level configuration templates
   - 动态权重调整
>    - Dynamic weight adjustment

3. **监控和报告**：
> 3. **Monitoring and Reporting**:
   - 状态流可视化面板
>    - State flow visualization panel
   - 效果评估报告
>    - Effectiveness evaluation reports
   - 异常检测告警
>    - Anomaly detection alerts

### 社区治理模式
> ### Community Governance Model

作为常驻内置技能，采用**社区共同治理**模式：
> As a resident built-in skill, adopts a **community co-governance** model:

1. **核心维护团队**：理论创建者 + 主要贡献者
> 1. **Core Maintenance Team**: Theory creator + main contributors
2. **社区审核委员会**：OpenClaw 社区代表
> 2. **Community Review Committee**: OpenClaw community representatives
3. **用户反馈机制**：定期收集和评估反馈
> 3. **User Feedback Mechanism**: Regularly collect and evaluate feedback
4. **版本发布流程**：严格的质量控制和测试
> 4. **Version Release Process**: Strict quality control and testing

### 安全性和隐私
> ### Security and Privacy

1. **数据最小化**：仅存储必要的状态流数据
> 1. **Data Minimization**: Only store necessary state flow data
2. **本地优先**：状态流数据默认本地存储
> 2. **Local First**: State flow data stored locally by default
3. **用户控制**：用户可随时禁用或调整
> 3. **User Control**: Users can disable or adjust at any time
4. **透明审计**：状态选择过程可审计
> 4. **Transparent Audit**: State selection process is auditable

## 📋 OpenClaw 规范符合性
> ## 📋 OpenClaw Specification Compliance

### 技能元数据
> ### Skill Metadata

| 字段 | 值 | 说明 |
|------|-----|------|
| name | haicd-state-engine | 技能名称 |
> | name | haicd-state-engine | Skill name |
| version | 2.0.0 | 语义化版本号（更新） |
> | version | 2.0.0 | Semantic version number (updated) |
| description | HAICD 状态引擎（常驻内置） | 简短描述 |
> | description | HAICD State Engine (Resident Built-in) | Brief description |
| author | Jeason, ZLXH | 作者信息 |
> | author | Jeason, ZLXH | Author information |
| license | CC BY-NC-SA 4.0 | 许可协议 |
> | license | CC BY-NC-SA 4.0 | License |
| triggers | [HAICD, ZLXH, ...] | 触发词列表 |
> | triggers | [HAICD, ZLXH, ...] | Trigger word list |
| resident_skill | true | 常驻技能标志 |
> | resident_skill | true | Resident skill flag |
| output_control_layer | true | 输出控制层标志 |
> | output_control_layer | true | Output control layer flag |

### 触发规则
> ### Trigger Rules

- ✅ 明确的触发词列表
> - ✅ Clear trigger word list
- ✅ 支持自动触发（默认启用）
> - ✅ Supports automatic triggering (enabled by default)
- ✅ 支持显式调用
> - ✅ Supports explicit invocation
- ✅ 支持常驻模式（用户授权后）
> - ✅ Supports resident mode (after user authorization)

### 技能执行
> ### Skill Execution

- ✅ 有清晰的执行流程
> - ✅ Has clear execution flow
- ✅ 有状态跟踪机制
> - ✅ Has state tracking mechanism
- ✅ 有配置管理
> - ✅ Has configuration management
- ✅ 有版本控制
> - ✅ Has version control
- ✅ 有历史感知能力
> - ✅ Has historical awareness capability
- ✅ 支持常驻运行模式
> - ✅ Supports resident operation mode
- ✅ 支持输出控制层集成
> - ✅ Supports output control layer integration

---

## 🔗 相关资源
> ## 🔗 Related Resources

| 资源 | 路径 |
|------|------|
| **理论文档** | `docs/HAICD-模型总览.md` |
> | **Theoretical Documents** | `docs/HAICD-模型总览.md` |
| **状态图谱** | `docs/haicd-state-graph.md` |
> | **State Graph** | `docs/haicd-state-graph.md` |
| **A 脚本** | `scripts/haicd_scoring_system.py` |
> | **A Script** | `scripts/haicd_scoring_system.py` |
| **B 脚本** | `scripts/state_flow_tracker.py` |
> | **B Script** | `scripts/state_flow_tracker.py` |
| **集成层** | `scripts/haicd_engine.py` |
> | **Integration Layer** | `scripts/haicd_engine.py` |
| **权重配置** | `config/haicd-weights.yaml` |
> | **Weight Configuration** | `config/haicd-weights.yaml` |
| **版本历史** | `VERSION.md` |
> | **Version History** | `VERSION.md` |

---

## 📄 许可协议
> ## 📄 License Agreement

**CC BY-NC-SA 4.0**

- **BY** (署名)：使用需注明理论创建者 Jeason
> - **BY** (Attribution): Must credit theory creator Jeason when using
- **NC** (非商业)：不得用于商业目的
> - **NC** (Non-Commercial): Cannot be used for commercial purposes
- **SA** (相同方式共享)：衍生作品使用相同许可
> - **SA** (Share Alike): Derivative works must use the same license

---

## 👥 致谢
> ## 👥 Acknowledgments

- **理论创建者**：Jeason（中国·石家庄）
> - **Theory Creator**: Jeason (Shijiazhuang, China)
- **技能实现**：智联星核 (ZLXH)
> - **Skill Implementation**: ZLXH
- **创建日期**：2026-03-27
> - **Creation Date**: 2026-03-27
- **技能版本**：v1.0.0
> - **Skill Version**: v1.0.0

---

## 📬 联系方式
> ## 📬 Contact Information

- **GitHub**: [待发布后填写]
> - **GitHub**: [To be filled after publication]
- **问题反馈**: [待发布后填写]
> - **Issue Feedback**: [To be filled after publication]

---

**技能版本**: v1.0.0  
> **Skill Version**: v1.0.0  
**最后更新**: 2026-03-27  
> **Last Updated**: 2026-03-27  
**状态**: ✅ 符合 OpenClaw 规范，A/B 脚本已集成
> **Status**: ✅ Complies with OpenClaw specifications, A/B scripts integrated