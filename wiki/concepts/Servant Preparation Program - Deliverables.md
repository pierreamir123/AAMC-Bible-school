---
type: concept
date: 2026-11-08
tags:
  - concept
  - servants
  - deliverables
ai-first: true
topic: servant-preparation-program-deliverables
related-projects:
  - "[[Bible School Curriculum Project]]"
confidence: medium
sources: "built from [[2026-11-08 - Vision Voice Note (transcript)]] and the Stage 1-6 notes; times, hours, weights and the 8-week length are proposals (اقتراح); church-related items flagged"
---

## For future agent
Index of the finished servant preparation program (Trident): four versioned PDF deliverables in `Deliverables/Servant Preparation Program/` (handbook, 8 session plans, assessment kit, templates). Latest release is v1.6 (v1.0 to v1.5 are kept untouched; v1.2 renamed the Trident axes, v1.3 added the Spirit axis components, v1.4 added the team-building stages). Lists what is inside, what still needs the owner's decisions, and how to publish the next version. Source decisions: [[Servant Program - Stage 2 Trident]], [[Servant Program - Stage 3 Assessment]], [[Servant Program - Stage 1 Structure]].

# برنامج إعداد الخدام: المخرجات النهائية

## الإصدارات
| الإصدار | التاريخ | ما فيه |
|---|---|---|
| **v1.6 (الأحدث)** | 2026-11-08 | الهيكل العظمي: عقلية القراءة والتناول التفاعلي والتفكير النقدي والبحث النقدي (وحدات ٢-٨ إلى ٢-١١، اقتراح) |
| v1.5 | 2026-11-08 | كود الهيكل العظمي «Walk the Talk» وقالب تقديم القصة (أسبوع ٥)، وملخص RASCI ومدد مراحل التيم كاقتراح |
| v1.4 | 2026-11-08 | مراحل بناء التيم (Forming، Storming، Norming، Performing) على كل تيم ومجموعة الخدام |
| v1.3 | 2026-11-08 | محور الروح: Mission، Vision، Culture، Identity، Branding، Communication flow وكود «Without system everything dies» |
| v1.2 | 2026-11-08 | تسمية المحاور: الروح والهيكل العظمي والجسد |
| v1.1 | 2026-11-08 | نفس المحتوى مع إصلاح تنسيق الـPDF (جداول، قوائم، فراغات، أسطر داخل الخلايا) |
| v1.0 | 2026-11-08 | الإصدار الأول |
المجلد: `Deliverables/Servant Preparation Program/` (فيه `README.md` و`CHANGELOG.md` و`LATEST.md` و`src/` و`tools/build.py`).

## محتوى الـ PDF الأربعة
| الملف | ما فيه |
|---|---|
| `01 - Program Handbook` | الرؤية، الخدمتان، الحارات الخمس، Trident، جدول ٨ أسابيع، شكل الجلسة (٩٠ د)، الأدوار، القواعد، معايير الإتمام، الحماية، القرارات المفتوحة |
| `02 - Session Plans` | خطة تفصيلية لكل أسبوع من ١ إلى ٨: الهدف، المخرج، الجدول الزمني، الأنشطة، المواد، مهمة الأسبوع، ملاحظات الميسّر، قياس النجاح |
| `03 - Assessment Kit` | المبادئ، نموذج الموافقة، استبيان الميول، ٢٥ بند مواقف، ٥ عينات عمل بمعايير، معادلة الملاءمة، قاعدة التوزيع، ورقة الميسّر، دليل المحادثة، مثال محسوب، الخصوصية |
| `04 - Templates and Handouts` | Code of conduct، جدول الاجتماع، تدفق التواصل، قائمة حماية الأطفال، موجز المنتج، «سفر في سطر»، قالب prompt وقائمة تحقق، ١٠ بطاقات أسئلة صعبة، متابعة الحضور، خطة تطوير شخصية |

## ما يحتاج قرارك قبل التشغيل
- الميسّر، والمراجع الكنسي، ومسؤول الحماية.
- موعد الاجتماع وبداية البرنامج (مقترح ٢٠٢٦-١١-١٥) وأعمار الخدام وامتحاناتهم.
- مدة الجلسة (٩٠ د) وعدد الأسابيع (٨): **اقتراحي**، التسجيل لا يحددهما.
- سياسة حماية الأطفال في الكنيسة (القوائم عامة مقترحة).
- اختيار الثيم (يؤثر في أسبوع ٣) ومكان تخزين درجات التقييم.
- الأوزان (٤٠/٣٠/٢٠/١٠) وأداة السمات (استبيان بسيط أم مقنَّن).

## كيف نصدر الإصدار التالي
عدّل `src/` ثم شغّل `build.py` بالرقم التالي (التفاصيل في `README.md`). كل إصدار يُحفظ في مجلده ولا يُستبدل.
