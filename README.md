# SCI Paper Writing Skill（Codex 版）

本技能整理自 2025 年《2周干完SCI写作教程与模版》中的六项核心写作方法，并增加对数值模拟论文、文献真实性、论文审查和写作日程的工作流支持。主入口为 `SKILL.md`，按需读取 `references/`，`assets/` 供实际论文起草时复制。

## 安装

**Linux/macOS/WSL：** 将文件夹 `sci-paper-writing` 放到个人 Skill 目录：

```bash
mkdir -p ~/.agents/skills
cp -r sci-paper-writing ~/.agents/skills/
```

**Windows PowerShell：**

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\sci-paper-writing" "$HOME\.agents\skills\"
```

若只在特定项目启用，复制到该项目的 `.agents/skills/sci-paper-writing/`。确认结构为 `.../sci-paper-writing/SKILL.md`（不要出现两层嵌套）。如 Codex 未立即发现新 Skill，开启新对话或重启 Codex 后试用。

## 使用示例

- `使用 $sci-paper-writing，根据我现有的研究内容设计3个符合 Computers and Geotechnics 风格的英文题目，并说明各自强调的贡献。`
- `使用 $sci-paper-writing，按“现状—局限—本文工作”组织我的 Introduction。不要编造引用。`
- `使用 $sci-paper-writing，读取这组CFD–DEM数据，依据图表写Results和Discussion，区分直接结果与机制推断。`
- `使用 $sci-paper-writing，只审查我最新的英文稿中逻辑、语法与学术风格问题，不直接修改文件。`
- `使用 $sci-paper-writing，根据现有材料生成14天SCI初稿计划；不把尚未完成的计算标为已完成。`

## 目录

```text
sci-paper-writing/
├── SKILL.md                    # 主入口：任务识别、证据规则、按需路由
├── README.md                   # 安装与调用方法
├── references/
│   ├── 01-title-and-abstract.md
│   ├── 02-introduction.md
│   ├── 03-methods-and-validation.md
│   ├── 04-results-and-discussion.md
│   ├── 05-conclusions.md
│   ├── 06-language-and-quality.md
│   ├── 07-14-day-plan.md
│   ├── 08-geotechnical-simulation.md
│   └── 09-source-map.md
├── assets/
│   ├── manuscript-outline.md
│   ├── evidence-matrix.csv
│   └── figure-analysis.md
└── scripts/
    └── audit_draft.py
```

## 内容边界

教程 PDF 不包含真正逐日安排；14 天计划是额外设计。参考文献“近五年占比”是经验而非期刊通用硬性要求。对无证据机理解释、未经独立验证的数值模拟结果，本 Skill 采用严格的科学写作规则而不是照搬宽松表达。原 PDF 未被复制入包；仍可单独作为学习资料查看。
