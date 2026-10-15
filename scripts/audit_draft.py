#!/usr/bin/env python3
"""Lightweight placeholder audit for Markdown, TXT, and DOCX manuscripts.

This is NOT a scientific, citation, plagiarism, or journal-format validator.
Standard library only. Usage: python audit_draft.py manuscript.docx
"""
import argparse
import re
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile
from xml.etree import ElementTree as ET

PATTERNS = [
    ("todo_marker", re.compile(r"\b(?:TODO|TBD|FIXME|CITATION\s+NEEDED)\b", re.I)),
    ("empty_citation", re.compile(r"\[(?:REF|REFERENCE|CITE|CITATION|SOURCE)\]", re.I)),
    ("placeholder_xx", re.compile(r"(?<![A-Za-z])X{2,}(?![A-Za-z])")),
    ("placeholder_figure", re.compile(r"\b(?:Fig(?:ure)?\.?|Table)\s+[X?](?!\w)", re.I)),
    ("placeholder_chinese", re.compile(r"\[(?:待补|需补|待核实|需提供|待填写|请填写|未确认)[^\]]*\]|【(?:待补|需补|待核实|需提供)[^】]*】")),
    ("placeholder_english", re.compile(r"\[(?:NEEDED|INSERT|PLACEHOLDER|FILL\s+IN)[^\]]*\]", re.I)),
]


def docx_paragraphs(path):
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with ZipFile(path) as archive:
        sources = ["word/document.xml"]
        sources.extend(x for x in archive.namelist() if re.fullmatch(r"word/(?:footnotes|endnotes)\.xml", x))
        for source in sources:
            if source not in archive.namelist():
                continue
            root = ET.fromstring(archive.read(source))
            for para in root.findall(".//w:p", ns):
                chunks = [t.text or "" for t in para.findall(".//w:t", ns)]
                if chunks:
                    yield "".join(chunks)


def load_text(path):
    ext = path.suffix.lower()
    if ext == ".docx":
        return "\n".join(docx_paragraphs(path))
    if ext in (".md", ".txt"):
        return path.read_text(encoding="utf-8-sig")
    raise ValueError("Supported extensions: .md, .txt, .docx")


def audit(text):
    issues = []
    for name, regex in PATTERNS:
        for match in regex.finditer(text):
            line_number = text.count("\n", 0, match.start()) + 1
            line = text.splitlines()[line_number - 1]
            snippet = line.strip()
            if len(snippet) > 150:
                snippet = snippet[:147] + "..."
            issues.append((line_number, name, snippet))
    return sorted(issues)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manuscript", type=Path)
    args = parser.parse_args()
    if not args.manuscript.exists():
        print(f"ERROR: file not found: {args.manuscript}", file=sys.stderr)
        return 2
    try:
        issues = audit(load_text(args.manuscript))
    except (ValueError, BadZipFile, ET.ParseError, UnicodeError, OSError) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2
    print(f"Scanned: {args.manuscript}")
    print(f"Placeholder findings: {len(issues)}")
    for line, name, excerpt in issues:
        print(f"L{line:<5} {name:<21} {excerpt}")
    print("Reminder: absence of placeholders does not imply scientific or citation correctness.")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
