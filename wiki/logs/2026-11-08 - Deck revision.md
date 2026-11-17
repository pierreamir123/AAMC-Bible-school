---
type: devlog
date: 2026-11-08
topic: AAMC deck revision (Structure and Journey Deck)
tags:
  - devlog
  - deliverables
  - presentation
related-projects:
  - "[[wiki/projects/Bible School Curriculum Project]]"
sources:
  - owner's slide-by-slide notes (Franco-Arabic), chat 2026-11-08
confidence: stated
ai-first: true
---

## For future agent
The owner dictated a slide-by-slide revision of `Deliverables/Structure and Journey Deck/deck.html` (Arabic RTL HTML deck). It went from 16 to 18 slides in Sinek order (Why, Who, What, How, When). The same edits were mirrored into `src/project/` (plain Slides-artifact fragments). Items marked "اقتراح" on the slides are my proposals, not the owner's words.

## What changed
- **New:** call-out (current generation, "co-wives" rivalry with non-Orthodox gatherings, light tone), "Start with Why" ribbon, fishbone summary (head = the dream; Spirit, Skeleton and Body above; Who, What and When below).
- **Deleted:** the two-codes slide (`codes`). `src/project/slides/codes.html` is kept on disk, only dropped from `deck.json` order.
- **Reworked:** Mission (person figure "مينا" plus element cards), Goal (onion rings of stakeholders), Structure ("What": school vs central service, pilot Grade 5 + Prep 1), Trident (servant = spirit / biblical = skeleton / contemporary = body, with verses), Spirit (new sublines, "Core" with periodicity and 2 Cor 4:16, RASCI card removed), Skeleton renamed "الشخصية" with teaching-method examples, Body (Design Thinking replaces the thinking council; Gen Alpha line), Milestones (the owner's 7 dates; years assumed Nov 2026 to Sep 2027).
- **Kept:** flow, bootcamp table, team stages, end goals, open items.

## Open points
- Owner's phrase "eston kol elmktob" (central service) was unclear; the slide says "كل ما يُنتَج للخدمة". Needs the owner's wording.
- Verse for "Servant = Spirit" (1 Cor 14:40) is my suggestion.
- Slides in `src/` are simplified text-only versions; the HTML deck has the drawings. The claude.ai Slides artifact is not re-published.
- Visual check was done on small screenshots (397px) plus a programmatic overflow check; not pixel-reviewed at full size.
