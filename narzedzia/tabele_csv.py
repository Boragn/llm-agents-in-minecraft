#!/usr/bin/env python3
"""Wyciaga tabele Markdown z rozdzialow eseju do CSV (dodatki/dane/tabele/<rozdzial>-tN.csv).

Uzycie: python3 -I narzedzia/tabele_csv.py   (z katalogu glownego eseju albo dowolnego, sciezki liczone od pliku)
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dodatki" / "dane" / "tabele"


def tabele(tekst):
    blok = []
    for l in tekst.splitlines() + [""]:
        if l.startswith("|"):
            blok.append(l)
        elif blok:
            yield blok
            blok = []


def komorki(l):
    return [c.strip().strip("*").replace("`", "") for c in l.strip().strip("|").split("|")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in sorted(ROOT.glob("czesc-*/*.md")):
        for n, b in enumerate(tabele(p.read_text(encoding="utf-8")), 1):
            wiersze = [komorki(l) for l in b if not re.match(r"^\|[\s:|-]+\|$", l)]
            f = OUT / ("%s-t%d.csv" % (p.stem, n))
            with open(f, "w", newline="", encoding="utf-8") as fh:
                csv.writer(fh).writerows(wiersze)
            print(f.relative_to(ROOT), len(wiersze) - 1, "wierszy")


if __name__ == "__main__":
    main()
