"""Build a new versioned release of the Servant Preparation Program PDFs.

Usage (from anywhere):
    python build.py v1.1 "what changed in one sentence"

Rules:
  - Edit the files in ../src/ (the working copy), then run this script with the NEXT version number.
  - A released folder (v1.0, v1.1, ...) is never overwritten; the script refuses if it exists.
  - Each release folder holds the PDFs plus a snapshot of the sources used (src/).
  - CHANGELOG.md and LATEST.md are updated automatically.
"""
import sys, re, shutil, subprocess, tempfile, datetime, difflib
from pathlib import Path
from urllib.parse import quote
import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FILES = [("01-handbook.md", "01 - Program Handbook"),
         ("02-session-plans.md", "02 - Session Plans"),
         ("03-assessment-kit.md", "03 - Assessment Kit"),
         ("04-templates.md", "04 - Templates and Handouts")]

CSS = """
@page { size: A4; margin: 16mm 14mm; }
html { direction: rtl; }
body { font-family: 'Segoe UI', Tahoma, Arial, sans-serif; font-size: 11pt; line-height: 1.65; color: #1c1c1c; direction: rtl; text-align: right; }
h1 { font-size: 22pt; margin: 0 0 6mm; padding-bottom: 3mm; border-bottom: 3px solid #1f4e79; color: #1f4e79; }
h2 { font-size: 15pt; margin: 8mm 0 3mm; color: #1f4e79; page-break-after: avoid; }
h3 { font-size: 12.5pt; margin: 5mm 0 2mm; page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 3mm 0 5mm; font-size: 10pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #9aa5b1; padding: 2mm 2.5mm; vertical-align: top; text-align: right; }
th { background: #e8eef5; }
blockquote { margin: 4mm 0; padding: 2.5mm 4mm; background: #f4f6f9; border-right: 4px solid #1f4e79; border-left: none; }
blockquote p { margin: 1mm 0; }
code, pre { direction: rtl; text-align: right; font-family: 'Segoe UI', Tahoma, Arial, sans-serif; background: #f4f6f9; }
pre { padding: 3mm; white-space: pre-wrap; border: 1px solid #c9d1da; }
ul, ol { padding-right: 7mm; padding-left: 0; }
li { margin: 1mm 0; }
.pb { page-break-after: always; }
"""

def fix_tables(text):
    out, prev = [], ""
    for line in text.splitlines():
        is_tbl = line.startswith("|")
        is_li = bool(re.match(r"(- |\d+\. )", line))
        prev_tbl = prev.startswith("|")
        prev_li = bool(re.match(r"(- |\d+\. |   )", prev))
        # a table or list must be separated from the paragraph before it,
        # and a paragraph must be separated from the table before it
        if prev.strip() and ((is_tbl and not prev_tbl) or (is_li and not prev_li and not prev_tbl)
                             or (prev_tbl and line.strip() and not is_tbl)):
            out.append("")
        out.append(line); prev = line
    return "\n".join(out) + "\n"

def die(msg):
    print("ERROR:", msg); sys.exit(1)

def main():
    if len(sys.argv) < 2 or not re.fullmatch(r"v\d+\.\d+", sys.argv[1]):
        die("usage: python build.py vMAJOR.MINOR \"change note\"")
    version = sys.argv[1]
    note = sys.argv[2] if len(sys.argv) > 2 else "(no note)"
    out = ROOT / version
    if out.exists():
        die(f"{out} already exists. Releases are never overwritten; use the next version.")
    if not Path(EDGE).exists():
        die("Microsoft Edge not found at " + EDGE)
    date = datetime.date.today().isoformat()

    # previous release (for the auto summary)
    prev = sorted([p for p in ROOT.glob("v*.*") if p.is_dir()], key=lambda p: [int(x) for x in p.name[1:].split(".")])
    prev = prev[-1] if prev else None

    out.mkdir(parents=True)
    (out / "src").mkdir()
    changed = []
    tmp = Path(tempfile.mkdtemp(prefix="spp_build_"))
    for fname, title in FILES:
        text = (SRC / fname).read_text(encoding="utf-8")
        text = text.replace("{{VERSION}}", version).replace("{{DATE}}", date)
        (out / "src" / fname).write_text(text, encoding="utf-8")
        if prev and (prev / "src" / fname).exists():
            old = (prev / "src" / fname).read_text(encoding="utf-8").replace(prev.name, "{{V}}")
            new = text.replace(version, "{{V}}")
            a = [l for l in old.splitlines()]
            b = [l for l in new.splitlines()]
            n = sum(1 for l in difflib.ndiff(a, b) if l[:2] in ("+ ", "- "))
            if n: changed.append(f"{fname} ({n} lines)")
        elif prev is None:
            changed.append(f"{fname} (new)")
        html_body = markdown.markdown(fix_tables(text), extensions=["tables", "fenced_code", "sane_lists"])
        html = f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><title>{title} ({version})</title><style>{CSS}</style></head><body>{html_body}</body></html>"
        h = tmp / (fname.replace(".md", ".html"))
        h.write_text(html, encoding="utf-8")
        pdf = out / f"{title} ({version}).pdf"
        prof = tmp / ("profile_" + fname)
        cmd = [EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={prof}",
               f"--print-to-pdf={pdf}", "file:///" + quote(h.as_posix(), safe="/:")]
        r = subprocess.run(cmd, capture_output=True, timeout=180)
        if not pdf.exists() or pdf.stat().st_size < 2000:
            die(f"PDF failed for {fname}: {r.stderr.decode('utf-8','ignore')[:300]}")
        print("built", pdf.name, pdf.stat().st_size // 1024, "KB")
    shutil.rmtree(tmp, ignore_errors=True)

    summary = ", ".join(changed) if changed else "no source changes"
    entry = f"## {version} · {date}\n- **ملاحظة:** {note}\n- **ملفات تغيّرت عن الإصدار السابق:** {summary}\n- **الملفات:** " + " · ".join(f"`{t} ({version}).pdf`" for _, t in FILES) + "\n\n"
    cl = ROOT / "CHANGELOG.md"
    head = "# سجل الإصدارات: برنامج إعداد الخدام\n\nالأحدث أولاً. كل إصدار في مجلده ولا يُستبدل.\n\n"
    old = cl.read_text(encoding="utf-8").split("\n\n", 2)[2] if cl.exists() and cl.read_text(encoding="utf-8").startswith("# سجل") else ""
    cl.write_text(head + entry + old, encoding="utf-8")
    (ROOT / "LATEST.md").write_text(f"# الإصدار الأحدث\n\n**{version}** · {date}\n\nالمجلد: `{version}/`\n\n{note}\n", encoding="utf-8")
    print("released", version)

if __name__ == "__main__":
    main()
