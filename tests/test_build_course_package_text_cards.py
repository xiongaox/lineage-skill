from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_course_package import build_package


def test_build_package_merges_text_evidence_cards(tmp_path: Path) -> None:
    course_dir = tmp_path / "course"
    cards_dir = course_dir / "text_distillation"
    cards_dir.mkdir(parents=True)
    cards = [
        {
            "card_id": "card-1",
            "card_type": "concept",
            "title": "证据优先",
            "summary": "先保留来源再综合。",
            "source_ref": "notes.md",
            "chunk_id": "chunk-1",
            "confidence": "medium",
        },
        {
            "card_id": "card-2",
            "card_type": "method",
            "title": "三步蒸馏",
            "summary": "采集、引用、压缩。",
            "source_ref": "notes.md",
            "chunk_id": "chunk-1",
            "confidence": "medium",
        },
        {
            "card_id": "card-3",
            "card_type": "quote",
            "title": "慢就是快",
            "quote": "慢就是快。",
            "source_ref": "notes.md",
            "chunk_id": "chunk-2",
            "confidence": "medium",
        },
        {
            "card_id": "card-4",
            "card_type": "boundary",
            "title": "证据边界",
            "summary": "没有来源就标记为推断。",
            "source_ref": "notes.md",
            "chunk_id": "chunk-3",
            "confidence": "medium",
        },
    ]
    (cards_dir / "evidence_cards.jsonl").write_text(
        "\n".join(json.dumps(card, ensure_ascii=False) for card in cards) + "\n",
        encoding="utf-8",
    )

    package = build_package("Demo", course_dir)

    assert any("证据优先" in item for item in package["concepts"])
    assert any("三步蒸馏" in item for item in package["methods"])
    assert any("慢就是快" in item for item in package["quotes"])
    assert any("证据边界" in item for item in package["boundaries"])
    assert any(row["type"] == "text_evidence_card" for row in package["evidence"])
