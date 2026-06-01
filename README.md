<div align="center">

# 师承.skill / Lineage Skill

**把课程材料蒸馏成可对话、可溯源、可复用的 AI Skill。**

面向 Codex / Claude Code / OpenClaw / Hermes / 自定义 Agent。

[![GitHub stars](https://img.shields.io/github/stars/JuneYaooo/lineage-skill?style=flat)](https://github.com/JuneYaooo/lineage-skill/stargazers)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Skill](https://img.shields.io/badge/AI%20Agent-Skill-orange.svg)](./SKILL.md)

```text
Course materials in, grounded expert skill out.
```

</div>

---

## 它解决什么

课程资料常见的问题不是“没有内容”，而是：

- 视频太长，复习只能拖进度条。
- 老师在哪一课讲过某个概念，很难找。
- AI 能总结，但经常没有来源。
- PPT、板书、图表、软件演示这些关键信息容易被纯转录丢掉。
- 学完后只剩散乱笔记，无法变成可调用的方法论。

`lineage-skill` 的目标是把课程变成一个能被 Agent 调用的知识系统。

## 它会生成什么

```text
课程材料
  ↓
CoursePackage
  ↓
多模式 AI Skill
```

核心产物：

- `course_package.json`：标准课程知识包，保存课时、概念、主题、案例、方法、金句、证据和边界。
- `SKILL.md`：告诉 Agent 什么时候触发、如何回答、如何引用、如何处理边界。
- `references/`：课程总览、课时索引、概念表、证据地图、金句、学习路径。
- `search_course_notes.py`：生成到 Skill 内的本地检索脚本。

## 真实案例

[JuneYaooo/nihaixia](https://github.com/JuneYaooo/nihaixia) 是通过这类课程蒸馏流程沉淀出来的真实 Skill 项目，来源包含 **100GB+ 视频课程材料**，最终整理成可触发、可检索、可溯源的专门领域 Skill。

## 怎么安装

把这句话发给你的 Agent：

```text
帮我安装 lineage-skill：
https://github.com/JuneYaooo/lineage-skill
```

然后让 Agent 检查需要配置的环境变量：

```text
安装这个课程蒸馏 Skill，并告诉我需要配置哪些环境变量。
```

具体执行规则在 [SKILL.md](./SKILL.md)，README 不写命令手册。

## 怎么使用

安装后直接用自然语言说需求。

```text
帮我把这个视频课程目录蒸馏成一个 course-expert skill。
它需要能回答课程问题、解释概念，并尽量给出来源。
```

```text
这个课程还有 PDF 讲义。请用 MinerU/OCR 解析 PDF，
再和视频转录、截图分析一起生成 CoursePackage 和 Skill。
```

```text
我已经有 transcripts、analysis、lesson_summaries 和 course_distillation 文件。
请直接构建 CoursePackage，并生成 course-expert,practitioner 组合模式的 Skill。
```

## Skill 模式

同一份课程可以生成不同用途的 Skill：

| Mode | 用途 |
| --- | --- |
| `course-expert` | 课程问答、概念解释、课时回查、来源引用 |
| `study-coach` | 学习计划、复习路径、回忆提示、反思提示 |
| `practitioner` | playbook、checklist、template、实操流程 |
| `citation-archive` | 强引用、原话检索、证据档案、可审计笔记 |
| `knowledge-base` | 多课程知识库、概念别名、跨课程主题图谱 |
| `domain-expert` | 多课程沉淀后的领域专家、方法库、案例库、边界规则 |

模式可以组合：

```text
请生成 course-expert,practitioner 两种模式组合的 Skill。
```

## 当前能力

| 能力 | 状态 |
| --- | --- |
| 视频转录 | 已支持 |
| 视频画面分析与关键截图 | 已支持 |
| PDF / MinerU OCR | 已接入主流水线 |
| 课程级蒸馏 | 已支持 |
| CoursePackage 构建 | 已支持 |
| 多模式 Skill 生成 | 已支持 |
| 本地关键词检索 | 已支持 |

## 配置与安全

复制 `.env.example` 为 `.env`，只填实际使用的服务。

- 音频转录：`AUDIO_TRANSCRIBE_*`
- 视觉分析：`LINEAGE_VISION_*`
- 文本蒸馏：`LINEAGE_TEXT_*`
- PDF / OCR：`MINERU_*`

安全原则：

- `.env` 不入库
- 不写死真实 token
- 不写死私有目录
- 不写死历史课程内容
- 转录、截图、OCR、蒸馏产物默认被 `.gitignore` 忽略

## 方法论

```text
Capture → Cite → Compress → Connect → Codify → Evaluate
采集      溯源    压缩        关联       技能化     评估
```

理论基础结合教学设计、认知学徒制、知识管理、多媒体学习和 RAG。详见 [THEORETICAL_FOUNDATION.md](./THEORETICAL_FOUNDATION.md)。

## 文档

- [SKILL.md](./SKILL.md) — Agent 使用入口和执行规则
- [METHODOLOGY.md](./METHODOLOGY.md) — C5 + Evaluate 方法论
- [THEORETICAL_FOUNDATION.md](./THEORETICAL_FOUNDATION.md) — 理论基础
- [SKILL_MODES.md](./SKILL_MODES.md) — 多模式 Skill 设计
- [ROADMAP.md](./ROADMAP.md) — 后续路线图

## License

Apache License 2.0. See [LICENSE](./LICENSE).
