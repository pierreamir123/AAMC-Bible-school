---
type: index
date: 2026-11-08
tags:
  - index
  - maintenance
ai-first: true
topic: orphan-notes
---

## For future agent
Index of orphan nodes in the vault: notes that no other note links to, plus unresolved ("ghost") links that point at notes that do not exist. Computed on 2026-11-08 by scanning every `.md` file for `[[wikilinks]]` (excluding `.obsidian/`, `.git/`, `.claude/` and `Deliverables/`, which only hold exported copies). Linking an orphan from this note gives it an incoming link; nothing here was deleted. Re-run the scan after big changes; the last count was 52 notes scanned, 2 orphans, 1 real ghost link.

# فهرس العقد اليتيمة (Orphans)

## ١) ملاحظات بلا أي رابط وارد
| الملاحظة | الحالة | الاقتراح |
|---|---|---|
| [[202611080530]] | ملف **فارغ** (٠ بايت)، بلا روابط واردة ولا صادرة، من الـ commit الأول. اسمه طابع زمني، أي أنه على الأرجح ملاحظة فارغة أُنشئت بالخطأ | **حذفه** بعد موافقتك (لم أحذفه) |
| [[Diagrams/_archived_/Service Frame.excalidraw\|Service Frame (مؤرشف)]] | رسم مؤرشف قديم؛ مذكور بالاسم في [[Diagrams - Index]] لكن بلا رابط | يُترك مؤرشفاً (مقصود). بهذا الفهرس صار له رابط وارد |

## ٢) روابط معلّقة (ghost links)
| الرابط | أين يرد | التقييم |
|---|---|---|
| `[[Welcome]]` | [[index]] و[[_CLAUDE]] | **حقيقي**: الملاحظة غير موجودة (الفهرس يقول إنها placeholder). إما أن تُنشأ وإما يُزال الرابط |
| `[[README]]` | [[index]] | **إنذار كاذب**: يشير إلى `Deliverables/Vault Notes PDF/README` المستبعد من المسح |
| `[[Person]]` `[[Related Project]]` `[[wikilinks]]` | [[_CLAUDE]] | **أمثلة نصية** في قواعد الكتابة، ليست روابط حقيقية |
| `1-storyteller.jpg` … `5-host.jpg` | الرسم المؤرشف Service Frame | صور مضمّنة غير موجودة؛ في أرشيف، لا إجراء |

## ٣) ما فُحص ولا مشكلة فيه
- لا توجد ملاحظة مرتبطة من `index.md` فقط (كل ملاحظة لها رابط من ملاحظة أخرى غير الفهرس).
- كل رسوم `Diagrams/01` إلى `10` مرتبطة من [[Diagrams - Index]].

## قرارات محتاجة منك
- [ ] حذف `202611080530.md` الفارغ؟
- [ ] إنشاء `Welcome` (صفحة هبوط حقيقية) أم إزالة رابطها؟
