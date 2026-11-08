---
type: log
date: 2026-11-08
tags:
  - deliverables
  - export
ai-first: true
---

## For future agent
How the PDF export of the vault's notes works. One script exports every Markdown note in `wiki/` and `Research/` (except `_archived_*`) to a PDF, plus one combined PDF with a table of contents. Each release gets its own folder and is never overwritten; the Markdown used is snapshotted inside it.

# تصدير الملاحظات PDF

| المسار | المحتوى |
|---|---|
| `v1.0/` | ٢٨ ملف PDF (واحد لكل ملاحظة) + `00 - All Notes (v1.0).pdf` المجمّع + `src/` لقطة المصادر |
| `tools/export.py` | يبني إصداراً جديداً |
| `CHANGELOG.md` · `LATEST.md` | سجل وآخر رقم |

**إصدار جديد:** `python "Deliverables/Vault Notes PDF/tools/export.py" v1.1 "ماذا تغيّر"` (يرفض رقماً موجوداً). المتطلبات: Python + مكتبة `markdown` + Microsoft Edge، وهي نفسها أداة [[Servant Preparation Program - Deliverables]].

**ما لا يشمله:** ملفات `_archived_*`، وملفات `raw/` (أصول لا تُعدَّل)، والرسومات `Diagrams/` (Excalidraw، لا تُصدَّر هنا).
