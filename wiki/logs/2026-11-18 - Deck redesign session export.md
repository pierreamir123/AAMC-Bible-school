---
type: devlog
date: 2026-11-18
topic: Export of the deck redesign chat (Small Beginnings deck)
tags:
  - devlog
  - deliverables
  - presentation
  - chat-export
related-people:
  - "[[Michael Safwat]]"
related-projects:
  - "[[wiki/projects/Bible School Curriculum Project]]"
sources:
  - chat session 2026-11-08 to 2026-11-18 (Claude Code)
confidence: stated
ai-first: true
---

## For future agent
This note exports the working session in which Pierre revised the Arabic HTML deck "بدايات صغيرة" (Small Beginnings) in `Deliverables/Structure and Journey Deck/`. It lists what he asked, what was built, which choices are mine (labeled "اقتراح" on the slides) and what is still open. The final deck has 14 slides. Earlier detail on the first revision is in [[wiki/logs/2026-11-08 - Deck revision]].

## Starting point
Pierre sent his slide-by-slide notes in Franco-Arabic. I turned them into a clean English prompt and then applied it to `deck.html` (16 slides at first, 1920x1080 fixed stage, RTL, wine/gold/ivory palette, Aref Ruqaa + IBM Plex Sans Arabic). Order follows Simon Sinek: Why, Who, What, How, When.

## Final slide order (14)
1. Cover: title **بدايات صغيرة**, verse Zechariah 4:10 starting "لا تحتقروا", background generated in Canva (open Bible with sprouts and a glowing cross).
2. Call-out: the current generation (Gen Alpha) and the "co-wives" (ضرائر) rivalry with non-Orthodox gatherings; Canva image of a child with a tablet.
3. Start with Why: onion rings with **Why** as the Core, then Who, What, How, When.
4. Dream (الحلم): original open-Bible drawing (I tried a Canva image and a vector scene, then reverted at his request).
5. Mission: dream broken into elements; icon of Onesimus (Wikimedia Commons, public domain); "Enablers" in brackets after مُمكِّنين.
6. Goal: Stakeholders as onion rings (servants, children, families as "Allies", services).
7. Structure ("What"): school service vs central service as 3D cubes; Pilot of 2 years (Grade 5 + Prep 1); 3 terms over 7 years.
8. The contemporary biblical servant: Spirit / Skeleton / Body with verses (1 Cor 14:40 is my suggestion; Luke 6:48; Rom 12:6) and a Canva figure of a glowing skeleton.
9. Spirit: Core in the centre (periodicity, 2 Cor 4:16) with Mission, Vision, Culture, Identity, Branding, Communication flow around it.
10. Personality (الشخصية): four thinking modes plus six teaching-method examples (suggestions).
11. Body: Gen Alpha in the centre, technical skills orbiting it.
12. Team Stages (Tuckman).
13. Milestones: winding-road timeline, 7 dates (11/11, 5/12, 1/1, 22/1, 1/2, 1/5, 15/9; years assumed Nov 2026 to Sep 2027).
14. Fishbone summary (head = the dream).

Removed along the way: two-codes slide, Boot Camp flow, Boot Camp 8-week table, End Goals, Open Items; the footer text "مدرسة الكتاب المقدس · الهيكل والرؤية" and several lines on the Structure slide (Personas, roles).

## Delivered files and links
- `Deliverables/Structure and Journey Deck/deck.html` (single file, images embedded) and `src/project/` (plain Slides-source mirror, partly out of date).
- `deck.pptx`: 14 slides, each a full-size picture of the HTML slide (not editable, no animation).
- Private claude.ai page: https://claude.ai/artifact/84aFj77QHV3TmJy5rwfyLD (published 2026-11-18; the in-page edit mode does not work there).
- Canva presentation rebuilt natively from the outline: https://canva.link/dskpblsht4vxdy6 (no custom drawings, no animations; animations must be added in Canva).
- Images generated in Canva and saved here: `cover-hero.jpg`, `callout-hero.jpg`, `servant-figure.jpg`; `dream-hero.jpg` is unused; `onesimus.jpg` is a Wikimedia Commons icon.

## Edited copy from Michael
A browser-saved copy of the deck (saved from `C:\Users\Michael\Downloads`, so probably [[Michael Safwat]]'s machine; confidence medium) contained his text edits, for example Mission title "أنا عاوز إيه من حضراتكم ؟" and Team Stages title "يللا نكون فريق .. بس لازم نعدى على مراحل!". I produced a cleaned copy (fonts restored, edit-mode leftovers and duplicate decorations removed, Fishbone and Team Stages layout fixed) on the Desktop, keeping every text edit. Possible typos left for the owner: "Gospel 27", "2027R&D", "الهيكلية".

## Open items
- Owner's wording for the central service ("eston kol elmktob") is still unclear.
- Years of the milestone dates are an assumption.
- Verse wording was typed from memory; verify against the printed Bible.
- Canva "Animate" must be applied by hand; the pptx has no motion.
- The `src/project` slides and the older Slides artifact (EBTnq5wAZGHUwQDM63xR63) were not updated to the final 14-slide look.
- Unrelated side question in the chat: an LM Studio model "Ternary-Bonsai-27B-dspark" failed to load because that file is a 3.6B `dspark` draft model, not the main weights.
