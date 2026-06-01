# MinerU / OCR Workflow

`lineage-skill` supports PDF OCR through MinerU. This is optional. Use it when course materials include scanned PDFs, lecture handouts, slide exports, or documents that should be part of the course evidence.

## What It Produces

MinerU outputs are stored under the course directory:

```text
<course>/
└── documents/
    ├── mineru/
    │   └── <document-id>/
    │       ├── full.zip
    │       ├── *.md
    │       └── ...
    ├── mineru_manifest.json
    └── mineru_supplement.md
```

`mineru_supplement.md` collects OCR Markdown text for course distillation.

## How Agents Should Use It

When the user says a course includes PDFs or scanned documents, the Agent should:

1. Check whether `MINERU_API_TOKEN` is configured.
2. Run MinerU parsing for PDF files or directories.
3. Build or update `mineru_supplement.md`.
4. Build `course_package.json`.
5. Generate or update the target Skill.

The README intentionally does not include shell commands. Execution details are in [SKILL.md](../SKILL.md).

## Rebuilding From Existing MinerU Output

If MinerU has already produced output, the agent can rebuild the supplement without submitting PDFs again by using the script's `--skip-submit` mode.

This is useful when:

- the API has already been called
- OCR output has been manually adjusted
- the user only wants to rebuild CoursePackage and Skill references

## Evidence Behavior

`build_course_package.py` records document OCR outputs as evidence:

```text
type: document_ocr
path: documents/.../*.md
granularity: file
```

`build_course_skill.py` also includes `documents/` files in `evidence_map.json`.

## Boundaries

- OCR quality depends on source PDF quality and MinerU output.
- OCR output should be treated as evidence, not automatically as final truth.
- For poor scans, formulas, tables, and diagrams may require manual review.
- Do not commit OCR outputs if source documents are private or copyrighted.

