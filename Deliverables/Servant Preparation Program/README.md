---
type: log
date: 2026-11-08
tags:
  - deliverables
  - servants
ai-first: true
---

## For future agent
How the Servant Preparation Program deliverables are organized and versioned. Four Arabic PDFs per release (handbook, session plans, assessment kit, templates) are built from Markdown sources by a script; each release gets its own folder and is never overwritten. Content decisions are in [[Servant Program - Stage 2 Trident]] and [[Servant Program - Stage 3 Assessment]].

# برنامج إعداد الخدام: المخرجات والإصدارات

## الهيكل
| المسار | المحتوى |
|---|---|
| `v1.1/` (الأحدث) | ٤ ملفات PDF + `src/` (لقطة المصادر المستخدمة) |
| `v1.0/` | الإصدار الأول (لا يُلمس) |
| `src/` | **نسخة العمل**: عدّل هنا ثم أصدر نسخة جديدة |
| `tools/build.py` | يبني الإصدار الجديد |
| `CHANGELOG.md` | سجل الإصدارات |
| `LATEST.md` | رقم الإصدار الأحدث |

## الملفات في كل إصدار
١. `01 - Program Handbook` دليل البرنامج · ٢. `02 - Session Plans` خطط الجلسات الثمانية · ٣. `03 - Assessment Kit` حقيبة التقييم · ٤. `04 - Templates and Handouts` النماذج

## كيف نصدر نسخة جديدة (كل تكرار)
١. عدّل الملفات في `src/`.
٢. شغّل (الرقم التالي، وجملة تصف التغيير):
```
python "Deliverables/Servant Preparation Program/tools/build.py" v1.2 "ماذا تغيّر"
```
٣. الأداة ترفض الرقم الموجود (لا استبدال)، وتحفظ لقطة المصادر في مجلد الإصدار، وتحدّث `CHANGELOG.md` و`LATEST.md`، وتكتب عدد الأسطر التي تغيّرت لكل ملف.
**قاعدة الترقيم (اقتراح):** رقم ثانوي (v1.1 ← v1.2) لتعديل أو تصحيح، ورقم رئيسي (v2.0) لتغيير في البنية أو القرارات الكبرى.

## ما يلزم لتشغيل الأداة
Python مع مكتبة `markdown`، ومتصفح Microsoft Edge (يُستخدم لتحويل HTML إلى PDF بدون واجهة).
