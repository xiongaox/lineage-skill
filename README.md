<div align="center">

# 师承.skill / Lineage Skill

**把看不完、找不到、用不起来的课程，变成可对话、可溯源、可复用的 AI Skill。**

面向 Codex / Claude Code / OpenClaw / Hermes / 自定义 Agent。  
适合把视频课、训练营、讲座、音频、PDF 讲义、截图证据和已有笔记，沉淀成能长期调用的课程专家。

[![GitHub stars](https://img.shields.io/github/stars/JuneYaooo/lineage-skill?style=flat)](https://github.com/JuneYaooo/lineage-skill/stargazers)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Skill](https://img.shields.io/badge/AI%20Agent-Skill-orange.svg)](./SKILL.md)

```text
Course materials in, grounded expert skill out.
```

</div>

---

## 你是不是也有这些问题

- 买了很多高价值课程，但复习时只能重新拖进度条。
- 课程视频几十 GB，老师讲过什么、在哪一课讲的，很难找。
- AI 可以总结，但经常说不清来源，无法判断哪些是真的来自课程。
- PPT、板书、图表、软件演示才是重点，但纯转录会丢掉这些结构信号。
- 想把一个老师/一套课的方法论沉淀下来，却最后只得到一堆散乱笔记。
- 课程学完了，但不会在真实问题里调用它。

`lineage-skill` 解决的不是“帮你写一篇课程总结”，而是把课程变成一个能被 Agent 调用的知识系统。

## 它把课程变成什么

| 原始状态 | 蒸馏后 |
| --- | --- |
| 一堆视频、音频、PDF、截图 | 一个结构化 `CoursePackage` |
| 只能按文件名找课 | 可按概念、主题、案例、方法、金句检索 |
| AI 回答没有出处 | 回答优先回到 transcript、analysis、screenshot、evidence |
| 学完就忘 | 可生成学习路径、回忆提示、专题笔记 |
| 方法论散在课时里 | 可封装成 course-expert / practitioner / citation archive 等 Skill |

最终得到的不是静态资料夹，而是一个可以继续问、继续查、继续复用的课程 Skill。

## 真实案例

[JuneYaooo/nihaixia](https://github.com/JuneYaooo/nihaixia) 是通过这类课程蒸馏流程沉淀出来的真实 Skill 项目，来源包含 **100GB+ 视频课程材料**，最终整理成可触发、可检索、可溯源的专门领域 Skill。

## 安装方式

把这句话发给你的 Agent：

```text
帮我安装 lineage-skill：
https://github.com/JuneYaooo/lineage-skill
```

或者说：

```text
安装这个课程蒸馏 Skill，并告诉我需要配置哪些环境变量。
```

README 只面向使用者。Agent 执行细节和脚本调用规则放在 [SKILL.md](./SKILL.md)。

## 使用方式

安装后直接用自然语言说你要处理什么课程、想生成什么 Skill。

### 把视频课变成课程专家

```text
帮我把这个视频课程目录蒸馏成一个 course-expert skill。
它需要能回答课程问题、解释概念，并尽量给出来源。
```

### 视频 + PDF 讲义一起处理

```text
这个课程还有 PDF 讲义。请用 MinerU/OCR 解析 PDF，
再和视频转录、截图分析一起生成 CoursePackage 和 Skill。
```

### 从已有蒸馏材料生成 Skill

```text
我已经有 transcripts、analysis、lesson_summaries 和 course_distillation 文件。
请直接构建 CoursePackage，并生成 course-expert,practitioner 组合模式的 Skill。
```

### 生成严格引用版本

```text
把这门课生成 citation-archive 模式。
回答时必须优先给课时、转录、截图或证据路径。
```

### 生成实操助手

```text
把这门课生成 practitioner 模式。
我希望它能把课程方法整理成 checklist、playbook 和模板。
```

## 能力一览

| 能力 | 状态 | 价值 |
| --- | --- | --- |
| 视频转录 | 已支持 | 把课程变成可检索文本 |
| 画面分析 + 关键截图 | 已支持 | 保留 PPT、板书、图表、软件演示 |
| PDF / MinerU OCR | 已接入主流水线 | 把讲义、扫描件并入课程包 |
| 课程级蒸馏 | 已支持 | 生成逐课摘要、概念、主题、方法、金句 |
| CoursePackage | 已支持 | 形成通用课程知识包 |
| 多模式 Skill 生成 | 已支持 | 同一门课可生成不同用途的 Skill |
| 本地关键词检索 | 已支持 | 快速查课程资料 |

## 可以生成哪些 Skill

| Mode | 适合什么 |
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

详细设计见 [SKILL_MODES.md](./SKILL_MODES.md)。

## 产物是什么

| 产物 | 说明 |
| --- | --- |
| `CoursePackage` | 标准课程知识包，包含 lessons、concepts、topics、cases、methods、quotes、evidence、boundaries |
| `SKILL.md` | Agent 触发条件、回答规则、引用规则、边界规则 |
| `references/` | 课程总览、课时索引、概念表、证据地图、金句、学习路径 |
| `search_course_notes.py` | 生成到 Skill 内的本地检索脚本 |
| mode-specific references | 学习计划、playbook、citation 规则、多课程索引等 |

## 配置什么

复制 `.env.example` 为 `.env`，只填实际使用的服务。

| 场景 | 变量 |
| --- | --- |
| 音频转录 | `AUDIO_TRANSCRIBE_API_KEY`, `AUDIO_TRANSCRIBE_BASE_URL`, `AUDIO_TRANSCRIBE_MODEL` |
| 视觉分析 | `LINEAGE_VISION_API_KEY`, `LINEAGE_VISION_BASE_URL`, `LINEAGE_VISION_MODEL` |
| 文本蒸馏 | `LINEAGE_TEXT_API_KEY`, `LINEAGE_TEXT_BASE_URL`, `LINEAGE_TEXT_MODEL` |
| PDF / OCR | `MINERU_API_TOKEN`, `MINERU_API_BASE`, `MINERU_MODEL_VERSION` |

安全原则：

- `.env` 不入库
- 不写死真实 token
- 不写死私有目录
- 不写死历史课程内容
- 转录、截图、OCR、蒸馏产物默认被 `.gitignore` 忽略

## 为什么可信

方法论是 C5 + Evaluate：

```text
Capture  →  Cite  →  Compress  →  Connect  →  Codify  →  Evaluate
采集        溯源      压缩          关联         技能化      评估
```

理论基础结合教学设计、认知学徒制、知识管理、多媒体学习和 RAG。详见 [THEORETICAL_FOUNDATION.md](./THEORETICAL_FOUNDATION.md)。

## 适合谁

| 你是谁 | 为什么适合 |
| --- | --- |
| 课程收藏很多的个人学习者 | 把看过的课变成可复习、可追问的长期资产 |
| 做培训/知识库的团队 | 把内部培训沉淀成可检索、可引用的团队 Skill |
| 想沉淀老师方法论的人 | 保留老师的概念、案例、判断和边界 |
| 做垂直领域 Agent 的开发者 | 从课程材料构建领域 Skill 和知识包 |
| 需要严格来源的人 | 用 citation-archive 模式保留证据链 |

## 项目文档

- [SKILL.md](./SKILL.md) — Agent 使用入口和执行规则
- [METHODOLOGY.md](./METHODOLOGY.md) — C5 + Evaluate 方法论
- [THEORETICAL_FOUNDATION.md](./THEORETICAL_FOUNDATION.md) — 理论基础
- [SKILL_MODES.md](./SKILL_MODES.md) — 多模式 Skill 设计
- [ROADMAP.md](./ROADMAP.md) — 后续路线图

## License

Apache License 2.0. See [LICENSE](./LICENSE).
