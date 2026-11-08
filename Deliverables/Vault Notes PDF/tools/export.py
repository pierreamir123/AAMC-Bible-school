"""Export every vault note (wiki/, Research/) to PDF as a new, never-overwritten release.

Usage:  python export.py v1.0 "what this release is"

Output: ../vX.Y/  one PDF per note, plus "00 - All Notes (vX.Y).pdf" (table of contents + every note),
        and a snapshot of the exact Markdown used in ../vX.Y/src/. Updates ../CHANGELOG.md and ../LATEST.md.
Reuses the CSS and table fixer of the Servant Preparation Program builder.
"""
import sys, re, shutil, subprocess, tempfile, datetime
from pathlib import Path
from urllib.parse import quote
import markdown

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT.parent.parent
sys.path.insert(0, str(VAULT / "Deliverables" / "Servant Preparation Program" / "tools"))
import build as spp  # CSS, fix_tables, EDGE

FIRST = ["Bible School Curriculum Project", "Church Vault - Vision and Servant System",
         "Habib Curriculum 2025 - Source Summary", "Research - Foundations for the Pillars",
         "Pillars - Topics and Vision", "Phase 1 - Bible Study Methods by Age", "Phase 1 - Gen Alpha and EdTech",
         "Phase 1 - Gamification of Scripture", "Service Lab v3 - Production Plan", "Curriculum v3 - Lectures by Term"]

def collect():
    files = [p for d in ("wiki", "Research") for p in (VAULT / d).rglob("*.md") if not p.stem.startswith("_archived_")]
    rank = {n: i for i, n in enumerate(FIRST)}
    return sorted(files, key=lambda p: (rank.get(p.stem, 100), p.stem))

def clean(text):
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)                       # frontmatter
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)                      # [[a|b]] -> b
    text = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).split("/")[-1], text)    # [[a/b]] -> b
    text = re.sub(r"^> \[!(\w+)\][-+]?\s*(.*)$", lambda m: f"> **{m.group(2) or m.group(1)}**", text, flags=re.M)
    return text

def page(title, body_md, version):
    body = markdown.markdown(spp.fix_tables(body_md), extensions=["tables", "fenced_code", "sane_lists"])
    return (f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><title>{title} ({version})</title>"
            f"<style>{spp.CSS}</style></head><body>{body}</body></html>")

def to_pdf(html, pdf, tmp, tag):
    h = tmp / f"{tag}.html"; h.write_text(html, encoding="utf-8")
    cmd = [spp.EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={tmp / ('p_' + tag)}",
           f"--print-to-pdf={pdf}", "file:///" + quote(h.as_posix(), safe="/:")]
    r = subprocess.run(cmd, capture_output=True, timeout=300)
    if not pdf.exists() or pdf.stat().st_size < 2000:
        sys.exit(f"PDF failed for {pdf.name}: {r.stderr.decode('utf-8', 'ignore')[:300]}")

def main():
    if len(sys.argv) < 2 or not re.fullmatch(r"v\d+\.\d+", sys.argv[1]):
        sys.exit('usage: python export.py vMAJOR.MINOR "note"')
    version, note = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "(no note)")
    out = ROOT / version
    if out.exists(): sys.exit(f"{out} exists. Releases are never overwritten.")
    if not Path(spp.EDGE).exists(): sys.exit("Edge not found")
    date = datetime.date.today().isoformat()
    out.mkdir(parents=True); (out / "src").mkdir()
    tmp = Path(tempfile.mkdtemp(prefix="vnp_"))
    notes = collect()
    combined = [f"# كل الملاحظات ({version})\n\nتاريخ التصدير: {date}. عدد الملاحظات: {len(notes)}.\n\n## الفهرس\n"]
    for i, p in enumerate(notes, 1):
        raw = p.read_text(encoding="utf-8")
        (out / "src").joinpath(p.name).write_text(raw, encoding="utf-8")
        md = clean(raw)
        to_pdf(page(p.stem, md, version), out / f"{p.stem} ({version}).pdf", tmp, f"n{i}")
        combined.append(f"{i}. {p.stem}")
        print("built", p.stem)
    body = ["\n".join(combined)]
    for p in notes:
        body.append("<div class='pb'></div>\n\n" + clean(p.read_text(encoding="utf-8")))
    to_pdf(page("All Notes", "\n\n".join(body), version), out / f"00 - All Notes ({version}).pdf", tmp, "all")
    shutil.rmtree(tmp, ignore_errors=True)
    entry = f"## {version} · {date}\n- **ملاحظة:** {note}\n- **عدد الملاحظات:** {len(notes)} (+ ملف مجمّع `00 - All Notes ({version}).pdf`)\n- **المحتوى:** كل ملفات `wiki/` و`Research/` عدا `_archived_*`\n\n"
    cl = ROOT / "CHANGELOG.md"
    head = "# سجل الإصدارات: تصدير الملاحظات PDF\n\nالأحدث أولاً. كل إصدار في مجلده ولا يُستبدل.\n\n"
    old = cl.read_text(encoding="utf-8").split("\n\n", 2)[2] if cl.exists() else ""
    cl.write_text(head + entry + old, encoding="utf-8")
    (ROOT / "LATEST.md").write_text(f"# الإصدار الأحدث\n\n**{version}** · {date}\n\nالمجلد: `{version}/`\n\n{note}\n", encoding="utf-8")
    print("released", version, len(notes), "notes")

if __name__ == "__main__":
    main()
