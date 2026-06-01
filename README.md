<div align="center">

# 师承.skill / Lineage Skill

**把任意课程蒸馏成可对话、可溯源、可复用的 AI Skill。**

面向 Codex / Claude Code / OpenClaw / Hermes / 自定义 Agent 的通用课程蒸馏框架：  
视频、音频、讲义、PDF、截图证据进来，生成 `CoursePackage`，再按用途包装成不同模式的专家 Skill。

[![GitHub stars](https://img.shields.io/github/stars/JuneYaooo/lineage-skill?style=flat)](https://github.com/JuneYaooo/lineage-skill/stargazers)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Skill](https://img.shields.io/badge/AI%20Agent-Skill-orange.svg)](./SKILL_MODES.md)

```text
Course materials in, grounded expert skill out.
```

</div>

---

## 为什么做这个

一门好课的价值通常不只是知识点，而是老师的结构、判断、案例、边界和反复强调的方法。问题是课程太长、复习太慢、引用不清，学完后很难真正调用。

`lineage-skill` 做的是课程资产化：

- 把长视频变成可检索转录
- 把 PPT、板书、图表、软件界面提取成视觉证据
- 把逐课内容压缩成摘要、概念、案例、方法、金句和边界
- 把整门课规范化为 `CoursePackage`
- 把 `CoursePackage` 包装成 Agent 可调用的 Skill

它不是课程总结器，而是课程知识系统生成器。

## 实际案例

[JuneYaooo/nihaixia](https://github.com/JuneYaooo/nihaixia) 就是通过这类课程蒸馏流程沉淀出来的真实 Skill 项目：把大量课程材料整理成可触发、可检索、可溯源的专门领域 Skill。

`lineage-skill` 是把这套能力抽象成通用框架，不绑定任何课程、老师、领域、私有路径或历史蒸馏内容。

## 当前能力

| 能力 | 状态 | 脚本 / 文件 |
| --- | --- | --- |
| 视频语音转录 | 已有 | `scripts/transcribe_video.py` |
| 视频画面分析 + 干货截图 | 已有 | `scripts/analyze_videos.py` |
| 课程级蒸馏 | 已有 | `scripts/distill_course.py` |
| 标准 CoursePackage | 已有 | `scripts/build_course_package.py` |
| 多模式 Skill 生成 | 已有 | `scripts/build_course_skill.py` |
| 一键流水线 | 已有 | `scripts/run_course_pipeline.py` |
| 本地关键词检索 | 已有 | 生成到 Skill 的 `scripts/search_course_notes.py` |
| PDF / OCR / MinerU 配置 | 已预留 | `.env.example` |

当前视频课程主链路已经可跑通。PDF、扫描件和 MinerU OCR 已在配置层预留；外部 OCR/MinerU 产物可以进入 `CoursePackage` 和 Skill 生成层。MinerU 解析命令接入主流水线是下一步。

## 整体架构

```text
Raw course materials
  ├─ videos / audio
  ├─ slides / PDF / docs
  └─ screenshots / notes
        ↓
Capture + Cite
  ├─ transcripts/*.json
  ├─ analysis/*_analysis.md
  └─ analysis/screenshots/*
        ↓
Compress + Connect
  ├─ lesson_summaries.json
  ├─ course_distillation_<date>.md/json
  └─ full_transcript.md
        ↓
CoursePackage
  └─ course_package.json
        ↓
Codify
  └─ dist/<skill-name>/
      ├─ SKILL.md
      ├─ references/*
      └─ scripts/search_course_notes.py
```

理论基础见 [THEORETICAL_FOUNDATION.md](./THEORETICAL_FOUNDATION.md)。方法论见 [METHODOLOGY.md](./METHODOLOGY.md)。

## 快速开始

```bash
git clone git@github.com:JuneYaooo/lineage-skill.git
cd lineage-skill
pip install -r requirements.txt
cp .env.example .env
```

编辑 `.env`，只填写你实际使用的 provider。不要提交 `.env`。

然后运行一键流水线：

```bash
python scripts/run_course_pipeline.py \
  --input-dir /path/to/course-videos \
  --course-name example-course \
  --skill-name example-course \
  --mode course-expert \
  --output-dir ./dist \
  --chunk-minutes 8
```

已经有转录或分析结果时，可以跳过阶段：

```bash
python scripts/run_course_pipeline.py \
  --input-dir /path/to/course-videos \
  --course-name example-course \
  --skill-name example-course-coach \
  --mode course-expert,study-coach \
  --skip-transcribe \
  --skip-analyze
```

## 分阶段使用

### 1. 转录视频

```bash
python scripts/transcribe_video.py \
  --input-dir /path/to/course-videos \
  --course-name example-course
```

输出：

```text
example-course/transcripts/*_transcript.json
```

### 2. 分析画面并提取截图

```bash
python scripts/analyze_videos.py \
  --input-dir /path/to/course-videos \
  --course-name example-course \
  --chunk-minutes 8
```

输出：

```text
example-course/analysis/*_analysis.md
example-course/analysis/screenshots/<video>/*.jpg
```

### 3. 蒸馏课程

```bash
python scripts/distill_course.py \
  --course-name example-course
```

输出：

```text
example-course/lesson_summaries.json
example-course/full_transcript.md
example-course/course_distillation_<date>.md
example-course/course_distillation_<date>.json
```

### 4. 生成 CoursePackage

```bash
python scripts/build_course_package.py \
  --course-name example-course \
  --source-dir ./example-course
```

输出：

```text
example-course/course_package.json
```

### 5. 生成 Skill

```bash
python scripts/build_course_skill.py \
  --course-name example-course \
  --skill-name example-course \
  --mode course-expert \
  --source-dir ./example-course \
  --output-dir ./dist
```

输出：

```text
dist/example-course/
├── SKILL.md
├── lineage_manifest.json
├── references/
│   ├── course_package.json
│   ├── course_digest.md
│   ├── full_transcript.md
│   ├── lesson_index.json
│   ├── concept_glossary.md
│   ├── evidence_map.json
│   ├── quote_index.md
│   └── study_paths.md
└── scripts/
    └── search_course_notes.py
```

## CoursePackage

`course_package.json` 是稳定中间层，不绑定课程领域：

```text
manifest
lessons
concepts
topics
cases
methods
learning_checks
quotes
evidence
study_paths
boundaries
quality
```

Skill 生成器优先读取 `course_package.json`，再回到 Markdown references 查细节和原文。

## Skill 模式

同一份课程可以生成不同用途的 Skill：

| Mode | 用途 |
| --- | --- |
| `course-expert` | 默认模式：课程问答、概念解释、课时回查、来源引用 |
| `study-coach` | 学习计划、复习路径、回忆提示、反思提示 |
| `practitioner` | playbook、checklist、template、实操流程 |
| `citation-archive` | 强引用、原话检索、证据档案、可审计笔记 |
| `knowledge-base` | 多课程知识库、概念别名、跨课程主题图谱 |
| `domain-expert` | 多课程沉淀后的领域专家、方法库、案例库、边界规则 |

组合模式：

```bash
python scripts/build_course_skill.py \
  --course-name example-course \
  --skill-name example-course-practice \
  --mode course-expert,practitioner \
  --source-dir ./example-course \
  --output-dir ./dist
```

详细设计见 [SKILL_MODES.md](./SKILL_MODES.md)。

## 环境变量

`.env.example` 只放占位变量，不包含真实 token、私有路径或课程内容。

```bash
# Audio transcription
AUDIO_TRANSCRIBE_API_KEY=
AUDIO_TRANSCRIBE_BASE_URL=https://your-audio-endpoint/v1
AUDIO_TRANSCRIBE_MODEL=whisper-1

# Vision analysis
LINEAGE_VISION_API_KEY=
LINEAGE_VISION_BASE_URL=https://your-vision-endpoint/v1
LINEAGE_VISION_MODEL=gpt-4o

# Text distillation
LINEAGE_TEXT_API_KEY=
LINEAGE_TEXT_BASE_URL=https://your-text-endpoint/v1
LINEAGE_TEXT_MODEL=gpt-4o

# Optional OCR / MinerU
MINERU_API_TOKEN=
MINERU_API_BASE=https://mineru.net/api/v4
MINERU_MODEL_VERSION=vlm
```

安全原则：

- `.env` 不入库
- 不写死真实 token
- 不写死私有目录
- 不写死历史课程内容
- 生成的转录、截图、蒸馏产物默认被 `.gitignore` 忽略

## 适合场景

| 场景 | 是否适合 |
| --- | --- |
| 把一门视频课变成可问答 Skill | 很适合 |
| 做课程复习、课时回查、概念整理 | 很适合 |
| 沉淀一个老师/课程体系的方法论 | 很适合 |
| 做带来源的课程知识库 | 适合 |
| 多课程合并成领域专家 | 规划中，已有模式设计 |
| 扫描 PDF 全自动接入 MinerU | 配置已预留，主命令待接入 |

## 项目结构

```text
.
├── README.md
├── METHODOLOGY.md
├── THEORETICAL_FOUNDATION.md
├── SKILL_MODES.md
├── ROADMAP.md
├── .env.example
├── examples/
└── scripts/
    ├── transcribe_video.py
    ├── analyze_videos.py
    ├── distill_course.py
    ├── build_course_package.py
    ├── build_course_skill.py
    ├── run_course_pipeline.py
    └── llm_client.py
```

## 路线图

- MinerU 解析命令接入主流水线
- OCR 结果到 CoursePackage 的标准映射
- 片段级 / 时间点级 evidence map
- 语义检索与向量索引
- 多课程合并与领域专家生成
- 用户反馈回流和质量评估增强

## 参考

- [JuneYaooo/nihaixia](https://github.com/JuneYaooo/nihaixia) — 由课程蒸馏流程产出的真实 Skill 项目
- [METHODOLOGY.md](./METHODOLOGY.md) — C5 + Evaluate 方法论
- [THEORETICAL_FOUNDATION.md](./THEORETICAL_FOUNDATION.md) — 理论基础
- [SKILL_MODES.md](./SKILL_MODES.md) — 多模式 Skill 设计

## License

Apache License 2.0. See [LICENSE](./LICENSE).
