# Claude Operating Manual - Pierre Bassily's Vault (AAMC Bible School)

> Read this file before doing anything in this vault.
> This is the single source of truth for how Claude operates here.

---

## Section 0 - AI-First Vault Rule (read first, applies to every note)

This vault is designed for **future agent** to read and reason over, not for human review. The owner calls Claude to retrieve, synthesize, and connect dots across accumulated knowledge.

**Every note Claude writes to this vault must follow these rules:**

1. **Self-contained context** - Each note must explain itself; it may be pulled via search with no surrounding context.
2. **"For future agent" preamble** - Every note begins with a 2-3 sentence plain-English summary.
3. **Rich, consistent frontmatter** - Filterable metadata (`type`, `date`, `topic`, `tags`, `related-people`, `related-projects`, `sources`, `confidence`).
4. **Recency markers per claim** - External facts carry a date: "X raised $24M (as of 2026-04)".
5. **Sources preserved verbatim** - Every external claim has its source URL inline.
6. **Cross-links are mandatory** - Every person, project, idea, decision, or concept uses `[[wikilinks]]`.
7. **Confidence levels** - Mark claims `stated | high | medium | speculation` where applicable.

This rule applies to all `/obsidian-*` and `/research*` commands, scheduled agents, and direct vault writes.

---

## Section 0.5 - Verify Live State Before Acting

Before declaring a bug, drafting a fix, or writing architecture: read the actual code, schema, deployed branch, env, or live data. Do not speculate from stale context. Fetch live dates and rates; never infer from training data.

---

## Vault Identity

- **Owner:** Pierre Bassily
- **Primary purpose:** AAMC Bible school - content, curriculum and planning (details TBD; update as the vault fills)
- **Vault style:** wiki
- **Last updated:** 2026-11-08

---

## Folder Map

| Folder | Purpose |
|---|---|
| `wiki/entities/` | People, companies, tools - one note each, told apart by `type:` |
| `wiki/concepts/` | Ideas, concepts, frameworks, synthesis, lesson/study material |
| `wiki/projects/` | Projects |
| `wiki/daily/` | Daily notes, `YYYY-MM-DD.md` |
| `wiki/logs/` | Work / dev logs |
| `wiki/reviews/` | Weekly / monthly reviews |
| `wiki/tasks/` | Standalone tasks and recurring obligations |
| `wiki/decisions/` | Decision records (ADRs) |
| `wiki/meetings/` | Meeting notes |
| `wiki/agenda/` | Agenda snapshots |
| `boards/` | Kanban boards |
| `raw/` | Immutable raw sources: `articles/`, `transcripts/`, `pdfs/`, `videos/` |
| `Research/` | Research output |
| `Bases/` | Obsidian Bases views (Projects, People, Tasks, Daily) |
| `Logs/` | Operations log, one file per day (`YYYY-MM-DD.md`) |
| `Diagrams/` | Excalidraw diagrams (`.excalidraw.md`); old drawings in `Diagrams/_archived_/` |
| `Deliverables/` | Versioned outputs (PDFs). One folder per program, one folder per release (`vX.Y`), never overwritten; sources in `src/`, builder in `tools/` |

---

## Key Files

- **Catalog:** `[[index]]` - read first when navigating the vault
- **Operations log pointer:** `[[log]]` (entries live in `Logs/`)
- **Landing note:** `[[Welcome]]`

---

## Active Context

**Current top priority:** TBD
**Current job:** TBD
**Manager:** TBD
**Key colleagues:** TBD

---

## Auto-Save Rules

Claude should auto-save the following **without asking**:
- Decisions made in conversation → `wiki/projects/` note + `wiki/daily/` note
- New people mentioned → `wiki/entities/` (create stub if needed)
- Tasks assigned or committed to → board in `boards/` + `wiki/tasks/` note
- Work done → `wiki/logs/` + project note + daily note

Claude should **ask before saving**:
- Anything involving finances or personal financial data
- Private notes
- Anything that deletes or archives an existing note

---

## Naming Conventions

- Daily notes: `YYYY-MM-DD.md`
- Work logs: `YYYY-MM-DD - Description.md`
- Tasks: descriptive title, no date prefix
- People: full name (e.g. `Jane Smith.md`)
- Archive prefix: `_archived_`

---

## Frontmatter Requirements

Every note must have at minimum:
```yaml
---
type: [note-type]
date: YYYY-MM-DD
tags:
  - [note-type]
ai-first: true
---
```

Note types: `daily` | `project` | `task` | `person` | `devlog` | `log` | `decision` | `meeting` | `review` | `source`. Full schema: `references/ai-first-rules.md` in the plugin, under "Type Schemas".

---

## Kanban Convention

Columns: `📥 Backlog` · `📋 This Week` · `🔨 In Progress` · `⏳ Waiting On` · `✅ Done`

Priority: 🔴 critical · 🟡 important · 🟢 low

Item format:
```
- [ ] 🔴 **Title** · @{YYYY-MM-DD}
	Description. [[Related Project]] [[Person]]
```

Completed: `- [x] ~~🔴 **Title**~~ ✅ Date`

---

## Propagation Rules

| Event | Also update |
|---|---|
| New project | Board (Backlog) + today's daily note |
| Task done | Board (Done, strikethrough) + project note + daily note |
| Work session | `wiki/logs/` + project note + daily note |
| Person interaction | Daily note + their `wiki/entities/` note |
| Decision made | Project note (Key Decisions) + daily note |

---

## People to Know

None recorded yet.

## Projects Currently Active

- [[wiki/projects/Bible School Curriculum Project]] - planning; 2-year gamified Bible curriculum + Service Lab

---

## Do Not Touch

- `raw/` - immutable sources; never edit after capture
- `Private/` - private; read only if directly asked

---

*This file was generated by the obsidian-second-brain skill.*
