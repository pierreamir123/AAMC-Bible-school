---
type: log
date: 2026-11-18
tags:
  - log
  - deliverable
ai-first: true
---

# Weekly Recap Game (٥ دقائق – ٥ إصحاحات)

**For future agent:** A single-file, offline, mobile-first Arabic (RTL) game played by servants at the start of the weekly meeting. 5 rounds, one per chapter read the previous week: timed quiz, lesson, personal commitment. Related: [[wiki/projects/Bible School Curriculum Project]].

## Use
- Send the `.html` file (WhatsApp / Drive); each person opens it on their phone. No internet needed.
- Each week: copy the latest file to a new `vX.Y/` folder and edit only the `GAME` block at the top (title + 5 rounds: `q`, `opts`, `a` = index of correct option, `verse`, `lesson`, `ask`, `commit`).
- Options are shuffled per phone; quiz timer is 20 s; total run ≈ 5 min.

## Releases
- v1.3 `week-01-nehemiah-1-5.html` (2026-11-18): story scenery + step-by-step wall. Each chapter has its own pixel-art scene with characters (ch1 messenger, burning gate, Nehemiah kneeling in prayer; ch2 king on throne + letter + moon; ch3 priest/goldsmith/girl builders hammering + sun; ch4 guard with spear, trumpeter, Sanballat and Tobiah mocking; ch5 poor man, nobleman with coin bag, table of bread). The wall is a continuous background; each chapter starts as charred ruins and is rebuilt brick by brick, one third per lesson coin; the flag rises on the last tower. Each round shows a one-line scene caption (`scene` field in `R`). v1.2 is superseded.
- v1.2 `week-01-nehemiah-1-5.html` (2026-11-18): the 5-minute version. Super Mario style, pixel-art Nehemiah avatar, same cream/burgundy/gold look as `Deliverables/Identity Workshop/workshop.html`. Per chapter the summary is merged to 3 lessons + 1 verse + 1 team question. Flow: run, jump to hit the "?" block (becomes a wall stone), tap 3 coins (3 lessons), next. End: wall builds and the flag rises, then pick a question to discuss. Sound is off by default (🔇 toggle). Edit only the `R` array at the top each week (`ch,title,motto,pts[3],verse,q`). Fonts load from Google when online, fall back to system fonts offline.
- v1.1 `week-01-nehemiah-1-5.html` (2026-11-18): redesigned per owner feedback. No quiz/score. Content taken from the owner's Google AI summary (reflections + application questions, same language). Progress = an SVG wall (one tower per chapter); each reflection read lays a stone, picking a question lays the gold capstone, Nehemiah 👷 walks along. End screen lists mottos and the questions the team picked for discussion. Edit only the `GAME` block: per round `ch,title,motto,cards[{h,t,v}],qs[]`. v1.0 (quiz version) is superseded.
- v1.0 `week-01-nehemiah-1-5.html` (2026-11-18): Nehemiah 1-5. Content written from general knowledge of the text (the shared Google AI link was not readable); verify verse wording before the meeting.

## Hosting (Firebase)
- Live: https://aamc-bible-school-recap.web.app (project `aamc-bible-school-recap`, created 2026-11-18).
- Weekly update: copy the newest game file to `site/public/index.html`, then from `Deliverables/Weekly Recap Game/site` run `npx firebase-tools deploy --only hosting`.
