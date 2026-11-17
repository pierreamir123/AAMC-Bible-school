---
type: log
date: 2026-11-18
topic: Chat export, AAMC deck revision (2026-11-08 session)
tags:
  - log
  - chat-export
  - deliverables
  - presentation
related-projects:
  - "[[wiki/projects/Bible School Curriculum Project]]"
related-people:
  - "[[Pierre Bassily]]"
sources:
  - "[[raw/transcripts/2026-11-08 - Deck revision dictation]]"
  - "[[wiki/logs/2026-11-08 - Deck revision]]"
confidence: high
ai-first: true
---

## For future agent
Export of the Claude Code chat in which Pierre dictated (in Franco-Arabic) a slide-by-slide revision of the Arabic HTML deck `Deliverables/Structure and Journey Deck/deck.html`, and Claude applied it. Read this for what was asked, what was decided, and what is still open. The build details are in [[wiki/logs/2026-11-08 - Deck revision]]; the verbatim dictation is in [[raw/transcripts/2026-11-08 - Deck revision dictation]].

## Timeline of the chat
1. **Prompt formatting.** Pierre pasted the Arabizi notes and asked for a clean prompt for the HTML deck. Claude produced an English prompt with the Arabic terms kept.
2. **Clarifications from Pierre.** "drayer" = ضرائر (co-wives: friendly rivalry with non-Orthodox gatherings). Old slide 6 is deleted ("fwrha" = delete it). Dates are day/month. The phrase "eston kol elmktob" (central service) was left unanswered.
3. **Plan, then build.** Questions answered: keep the unmentioned slides, replace the Milestones slide, fishbone as a final summary, edit both `deck.html` and `src/project/slides`. Result: 16 slides became 18 in Sinek order (Why, Who, What, How, When).
4. **Trim.** Pierre asked to remove the last two slides (End Goals, Open Items). The deck is now 16 slides, ending with the fishbone.
5. **Visuals.** Slide 9 (Spirit) was redesigned with the same concept: a radial map with icons, a Core card with 2 Corinthians 4:16, and a "how to read" card.
6. **Terminology.** Widely used English terms stay in English: Milestones, Fishbone, Goal: Stakeholders, Mission (title), Team Stages, Boot Camp, Team.
7. **Not done.** Pierre asked to enhance the visuals further using their Gemini browser account or Canva for generated images and vectors; that request was interrupted before any work started.
8. **This export** and a push to GitHub (commit on `main`).

## Decisions (owner)
- Start with the Why (Simon Sinek order): Why, Who, What, How, When.
- Vision is framed as a dream (حلم). A call-out about the current generation comes first.
- Servant = Spirit (verse about order), biblical = Skeleton (Luke 6:48), contemporary = Body (Romans 12:6).
- "Core" replaces "system", with periodicity in the middle and 2 Corinthians 4:16. Responsibility (RASCI) is removed from the Spirit slide.
- Skeleton is renamed "الشخصية" (Personality). "Thinking council" becomes Design Thinking.
- Milestones, as day/month: 11/11, 5/12, 1/1, 22/1, 1/2, 1/5, 15/9 (years Nov 2026 to Sep 2027 assumed).

## Proposals by Claude (labeled "اقتراح" on the slides)
- 1 Corinthians 14:40 as the "order" verse for Spirit.
- Teaching-method examples on the Personality slide.
- The persona figure named "مينا" on the Mission slide.

## State at push time (2026-11-18)
This chat ended with a 16-slide `deck.html`. When pushed, `deck.html` had 14 slides, plus `deck.pptx` and hero images (`cover-hero`, `callout-hero`, `dream-hero`, `servant-figure`, `onesimus`): another session changed the deck after this chat. Those later edits are not described here; check the deck README and git log.

## Open
- Wording of "eston kol elmktob" for the central service.
- Verse wording (all four) was written from memory; check against the printed Bible.
- Image and vector enhancement via Gemini or Canva: not started.
- `src/` slides are text-only; the claude.ai Slides artifact was not re-published.
- A separate fork of this chat produced a cleaned copy of another deck on the Desktop ("بدايات صغيرة ... (مصحح).html"); that file is outside this vault.
