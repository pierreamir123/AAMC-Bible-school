---
type: concept
date: 2026-11-08
tags:
  - concept
  - servants
  - trident
  - trident-bootcamp
  - architecture
  - diagrams
ai-first: true
topic: trident-bootcamp-architecture
related-projects:
  - "[[Bible School Curriculum Project]]"
confidence: high
sources: "Owner request on 2026-11-08 adopting 'Trident Bootcamp' as the official terminology replacing 'إعداد خدمة'; vision details from [[2026-11-08 - Vision Voice Note (transcript)]]; foundational framework from [[Servant Program - Stage 2 Trident]]"
---

## For future agent
This document defines the architecture, visual diagram, and operational flow of the **Trident Bootcamp**, which officially replaces the legacy term "إعداد خدمة" (servant preparation). The bootcamp is an 8-week intensive pathway structured around the three prongs of the Fork/Trident Strategy (Structure, Biblical skills, Technical skills), concluding with a psychological & capability assessment that places servants into 5 parallel persona lanes.

# Trident Bootcamp (معسكر الترايدنت لإعداد الخدام)

> **تحديث المصطلحات (2026-11-08):** تم اعتماد اسم **Trident Bootcamp** رسمياً ليكون التعبير الأساسي والبديل عن تعبير «إعداد خدمة» أو «برنامج إعداد الخدام».

---

## 1. المخطط الهيكلي (Trident Architecture Diagram)

```mermaid
graph TD
    classDef main fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef prong1 fill:#064e3b,stroke:#10b981,stroke-width:1.5px,color:#fff;
    classDef prong2 fill:#1e3a8a,stroke:#3b82f6,stroke-width:1.5px,color:#fff;
    classDef prong3 fill:#581c87,stroke:#a855f7,stroke-width:1.5px,color:#fff;
    classDef gate fill:#881337,stroke:#f43f5e,stroke-width:2px,color:#fff;
    classDef lanes fill:#0f172a,stroke:#64748b,stroke-width:1.5px,color:#fff;
    classDef outcome fill:#14532d,stroke:#22c55e,stroke-width:2px,color:#fff;

    Root["🔱 Trident Bootcamp<br/><b>معسكر الترايدنت لإعداد الخدام</b><br/><i>(الرؤية والاصطفاف - الأسبوع ١)</i>"]:::main

    Root --> P1["<b>Prong 1: Structure & Culture</b><br/>(الأسابيع ٢–٣)"]:::prong1
    Root --> P2["<b>Prong 2: Biblical Skills</b><br/>(الأسابيع ٤–٥)"]:::prong2
    Root --> P3["<b>Prong 3: Technical Skills</b><br/>(الأسابيع ٦–٧)"]:::prong3

    subgraph SubStructure ["شعبة الهيكل والانضباط (Structure)"]
        P1 --> S1["Code of Conduct & Discipline"]
        P1 --> S2["الاجتماع الأسبوعي ووقت الصلاة الثابت"]
        P1 --> S3["Hierarchy & Communication Flow"]
        P1 --> S4["هوية الخدمة وشخصية 'مورو' (Branding & Mascot)"]
    end

    subgraph SubBiblical ["شعبة العمق الكتابي (Biblical Skills)"]
        P2 --> B1["T-Strategy: بانوراما أفقية + عمق رأسي"]
        P2 --> B2["منهجية القراءة: أقرأ ← أدرس ← أفهم ← أعيش ← أكرز"]
        P2 --> B3["الخرائط والجغرافيا وسياق العهدين"]
        P2 --> B4["ضوابط الرموز والرد على الأسئلة الصعبة"]
    end

    subgraph SubTechnical ["شعبة التقنية والابتكار (Technical Skills)"]
        P3 --> T1["AI Literacy & الهندسة الفعالة للـ Prompts"]
        P3 --> T2["تدقيق مخرجات الـ AI واكتشاف الهلوسة والتحيز اللاهوتي"]
        P3 --> T3["سيكولوجية التعليم وديناميكيات جيل ألفا (Gen α)"]
        P3 --> T4["حماية الأطفال وخصوصية البيانات وتصميم الألعاب"]
    end

    S1 & S2 & S3 & S4 & B1 & B2 & B3 & B4 & T1 & T2 & T3 & T4 --> Gate["<b>بوابة التقييم والتوزيع (الأسبوع ٨)</b><br/>Psychological & Capability Assessment Gate"]:::gate

    Gate --> L1["حارة الراوي<br/><b>Storyteller</b>"]:::lanes
    Gate --> L2["حارة صاحب الرؤية<br/><b>Visionary</b>"]:::lanes
    Gate --> L3["حارة الشرارة<br/><b>Spark</b>"]:::lanes
    Gate --> L4["حارة الحارس<br/><b>Keeper</b>"]:::lanes
    Gate --> L5["حارة المضيف<br/><b>Host</b>"]:::lanes

    L1 & L2 & L3 & L4 & L5 --> Teams["تشكيل فرق العمل الميدانية الرشيقة<br/><b>Agile Pods & Teams</b>"]:::main

    Teams --> Target1["<b>الخدمة الدراسية (Study Service)</b><br/>مدرسة الكتاب المقدس (٧ سنين: ب٣ إلى ع٣)"]:::outcome
    Teams --> Target2["<b>الخدمة المركزية (Central Service)</b><br/>مصنع المنتجات الرقمية والحسية (Digital & Physical)"]:::outcome
```

---

## 2. المحاور الثلاثة لشعبة الترايدنت (The 3 Prongs)

### ١. المحور الأول: Structure & Culture (النظام والانضباط)
* **Code of Conduct & Discipline:** ميثاق مكتوب يحدد التزامات الخادم، السلوك الروحي، ومواعيد الحضور.
* **الاجتماع الأسبوعي والصلاة:** توقيت أسبوعي صارم يبدأ بصلاة مشتركة، دراسة كتابية للخدام، وورشة تدريبية.
* **Hierarchy & Communication:** وضوح قنوات التواصل وتدفق التوجيهات بدون عشوائية.
* **Service Identity:** إطلاق هوية الخدمة البصرية (Branding)، واختيار ألوانها وشخصية المورو / Mascot.

### ٢. المحور الثاني: Biblical Skills (المهارات الكتابية - T-Strategy)
* **T-Strategy:** 
  * الخط الأفقي: مسح شامل للأسفار الـ 66 بعنوان "سفر في سطر" لفهم البانوراما الكتابية.
  * الخط الرأسي: دراسة معمقة للنصوص وتفسيرها لاهوتياً وتاريخياً.
* **منهجية القراءة الخماسية:** (أقرأ ← أدرس ← أفهم ← أعيش ← أكرز).
* **الجغرافيا والخرائط:** ربط القصص بمواقعها الحقيقية على الخرائط التفاعلية.
* **الأمان اللاهوتي:** استناد التعليم للكتاب المقدس وعقيدة الكنيسة وضوابط الرمز في المسيح.

### ٣. المحور الثالث: Technical Skills (المهارات التقنية والابتكارية)
* **AI Literacy & Prompt Engineering:** تمكين الخادم من استخدام الذكاء الاصطناعي لإنتاج الأنشطة والوسائط دون كسل ذهني.
* **تدقيق الذكاء الاصطناعي:** فحص هلوسة الـ AI وكشف أي انحرافات لاهوتية أو تربوية.
* **علم نفس النمو وجيل ألفا (Gen Alpha):** فهم طبيعة انتباه الأطفال الرقمي واحتياجاتهم التفاعلية.
* **Child Protection & Gamification:** سياسات حماية النشء وتصميم الألعاب التنافسية الهادفة.

---

## 3. مسار الأسابيع الثمانية (The 8-Week Bootcamp Schedule)

| الأسبوع | المرحلة | الهدف والمخرجات |
|---|---|---|
| **الأسبوع ١** | **الرؤية والاصطفاف (The Vision)** | فهم استراتيجية الترايدنت، الرؤية المزدوجة (الخدمة الدراسية + الخدمة المركزية). |
| **الأسابيع ٢–٣** | **بلوك الهيكل والنظام (Structure)** | إقرار الـ Code of Conduct، تثبيت مواعيد الصلاة والاجتماع، تدشين الهوية وشخصية مورو. |
| **الأسابيع ٤–٥** | **بلوك العمق الكتابي (Biblical)** | ورش عمل T-Strategy، الخرائط التفاعلية، وتطبيق منهجية القراءة الخماسية عملياً. |
| **الأسابيع ٦–٧** | **بلوك التقنية والـ AI (Technical)** | معمل البرومتات، إنتاج نماذج ألعاب تفاعلية، ومواءمة المحتوى لخصائص جيل ألفا. |
| **الأسبوع ٨** | **بوابة التقييم والتوزيع (Placement)** | التقييم النفسي والمهاري، التسكين في الحارات الخمس، وإطلاق الفرق الميدانية. |

---

## 4. هندسة الجلسة الأسبوعية (Session Architecture - 90 Minutes)

1. **١٠ دقائق:** صلاة وافتتاح روحي مشترك.
2. **١٠ دقائق:** مراجعة إنجازات وتحديات الأسبوع السابق.
3. **٥٠ دقيقة:** المحتوى الأساسي وورشة العمل (طبقاً لموضوع الأسبوع).
4. **١٥ دقيقة:** تطبيق عملي معملي في مجموعات صغيرة (Lab / Simulation).
5. **٥ دقائق:** صلاة ختامية وتكليف الأسبوع.

---

## 5. روابط ذات صلة (Vault Cross-Links)
- [[Diagrams/05 - Trident Program.excalidraw|05 - Trident Program]] (مخطط الإكسكاليدرو)
- [[Servant Program - Stage 2 Trident]] (مسودة المرحلة ٢ التفصيلية)
- [[Servant Program - Stage 3 Assessment]] (أدوات التقييم والتوزيع على الحارات)
- [[2026-11-08 - Vision Voice Note (transcript)]] (التسجيل الصوتي المؤسس للرؤية)
- [[Diagrams - Index]] (فهرس المخططات بالكامل)
