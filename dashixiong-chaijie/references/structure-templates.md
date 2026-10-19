# 方法论标尺② — 结构 / 方法 / 句式模板

> 本文档是拆维①结构、维③方法、维④句式时用的**标尺**。把论文对回这些「八股文模板」，看它哪里合规、哪里越界、哪里可复用。

---

## 一、论文类型判断（Step 0 用）

| 论文类型 | 判断信号 | 方法链条特点 |
|---------|---------|-------------|
| **机制类** | 题目含 mechanism；创新在「揭示/探明机理」 | 现象 → 机制解释 |
| **实验类** | 题目含 experimental investigation；创新在「开展试验」 | 材料→设备→设计→步骤→现象 |
| **新方法/新技术/新模型类** | 题目含 novel model/method/technique；创新在「提出模型」 | 提出 → 标定 → 验证 → 应用 |
| **综述类** | 题目含 review/state-of-the-art | 无原创方法，按问题维度组织文献 |

---

## 二、Abstract 八句结构

```
句1 | 背景 + 研究对象
句2 | 问题引入 + 重要性
句3 | 问题紧迫性 / 已有研究不足
句4 | 本文核心工作——做了什么
句5 | 本文核心工作展开——怎么做的
句6 | 核心发现 1
句7 | 核心发现 2 + 补充
句8 | 贡献与意义
```

**拆解动作**：把 Abstract 逐句对回 8 个槽位，标出「创新点在第 4-5 句」「核心发现在第 6-7 句」是否到位。缺哪句，就说明作者包装得不够满。

---

## 三、Introduction 三段式 / 四段式

### 三段式（最简）
```
第1段 | 大背景 → 小背景 → 具体问题及重要性
第2段 | 文献综述（按问题分类，不按时间流水账）
第3段 | 本文目标 + 开展的工作 + 主要结论
```

### 四段式（更常见，把「不足」单独成段）
```
第1段 | 研究背景（大背景 → 具体问题）
第2段 | 现有研究进展（文献综述）
第3段 | 现有研究不足 ⬅ 重点！与创新点呼应
第4段 | 本研究（提出什么、有何优势、预期成果）
```

**「现有研究不足」段落模板**（拆解时重点看这段写得好不好）：
```
However, existing studies have several limitations. First, [具体不足1],
which leads to [不利影响1]. Second, [具体不足2], making it difficult to
[不利影响2]. Third, limited attention has been paid to [被忽视的问题],
despite its importance in [重要性]. These gaps motivate the need for [本研究].
```

**文献综述的分类维度**（判断作者是高手还是菜鸟）：
- ✅ 高手：按问题 / 按方法 / 按研究方式分类
- ❌ 菜鸟：按时间记流水账（"A 做了 X，B 做了 Y，C 做了 Z"）

---

## 四、Results 五步法

每个「发现」是否走全了五步（越全，分析越深、越接近一二区）：

```
Step 1 | 标图：Fig. X presents/shows [展示内容]
Step 2 | 趋势：It is found that XX [increases/decreases/varies] with YY
Step 3 | 机制：This can be attributed to... / The underlying mechanism is that...
         （First, ... Second, ...）
Step 4 | 文献支撑：This is consistent with XX [1] / supported by the work of XX
Step 5 | 意义：These findings have implications for... / provide reference for...
```

**拆解动作**：数一数作者每个发现走完了几步。只走 Step 1-2 = 三区水平；走到 Step 3（机制）= 二区水平；走全五步 = 一区水平。这是衡量论文「分析深度」的硬指标。

**从数据到机制的过渡句式**（可挖空复用）：
```
This behavior can be understood by considering [机制]...
The observed [现象] is attributed to [机制], whereby [解释过程]...
This trend is consistent with [已知理论], which predicts that [预期]...
```

---

## 五、Conclusion 帽子 + 干条

```
帽子段 | 总结全文工作（In this study, ... were conducted to investigate...）
       （This paper presented a novel XX model for...）
逐条结论 | 3-5 条编号结论（每条 = 一条核心发现/创新点）
```

**拆解动作**：结论是否「帽子 + 干条」？每条结论是否具体、有证据、有工程普适性（而非只适用特定工况的废话）？

---

## 六、研究方法链条模板（拆维③方法套路用）

拆维③时，先按论文类型套对应模板，把方法拆成一条「可复制」的链。

### 实验类
```
实验材料 → 实验设备 → 实验设计（工况表）→ 实验步骤 → 实验现象 → 机理揭示
```
关键点：对照组设置、干扰因素排除（边界效应/环境因素如何控制）。

### 数值模拟类
```
工程背景 → 数值模型（本构/参数/标定方法）→ 模型验证（试验/实测/理论对比）→ 计算工况 → 结果分析 → 机理揭示
```
**必拆两步**：
- **参数标定**：参数从哪来？如何确定？有没有敏感性分析？（审稿人最关注）
- **模型验证**：用什么验证的？精度如何？（验证不充分 = 硬伤）

### 理论推导类
```
理论简介 → 推导过程 → 验证（试验/实测/数值）→ 算例分析 → 参数分析
```

**可复制性标注**：拆完方法链后，用一句话标注「照做需要什么」——例如「1 组三轴实验 + 1 组数值模拟 + 简单对比 = 一篇三区」或「需要自建实验装置 + 长期野外监测，门槛高」。

---

## 七、连接词库 + 句式信号

### 转折（找 Gap / 不足的标记词）
```
However, Nevertheless, Despite, Although, Unfortunately, 
...but..., ...while..., ...yet...
```

### 本文工作（找创新点的标记词）
```
In this paper, Here we present/propose, To address this, We developed, 
The key innovation is, Unlike previous, To the best of our knowledge, this is the first...
```

### 机制归因（找分析深度的标记词）
```
attributed to, because of, due to, owing to, The underlying mechanism is that,
Two factors contribute: First, ... Second, ...
```

### 结论/意义
```
The results demonstrate/indicate/suggest that..., These findings have implications for...,
This provides a practical tool for...
```
