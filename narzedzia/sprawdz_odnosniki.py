#!/usr/bin/env python3
"""Sprawdza wszystkie wzgledne linki i obrazy w plikach Markdown eseju (poza _prywatne/).

Uzycie: python3 -I narzedzia/sprawdz_odnosniki.py [KATALOG] [--z-prywatnymi]
Kod wyjscia 0 = wszystkie cele istnieja, 1 = sa zepsute odnosniki. Linki http(s) i kotwice (#...) sa pomijane
(kotwica po pliku jest odcinana, sprawdzany jest tylko plik).
"""
import re
import sys
from pathlib import Path

LINK = re.compile(r"!?\[(?:[^\[\]]|\[[^\]]*\])*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def sprawdz(root, z_prywatnymi=False):
    zle, ile = [], 0
    for p in sorted(root.rglob("*.md")):
        if "_prywatne" in p.parts and not z_prywatnymi:
            continue
        w_kodzie = False
        for nr, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if l.strip().startswith("```"):
                w_kodzie = not w_kodzie
                continue
            if w_kodzie:
                continue
            for m in LINK.finditer(l):
                cel = m.group(1)
                if re.match(r"^(https?:|mailto:|#)", cel):
                    continue
                ile += 1
                plik = cel.split("#", 1)[0]
                if not (p.parent / plik).resolve().exists():
                    zle.append((p.relative_to(root), nr, cel))
    return ile, zle


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    root = Path(a[0]) if a else Path(__file__).resolve().parents[1]
    ile, zle = sprawdz(root, "--z-prywatnymi" in sys.argv)
    print("ODNOSNIKI: sprawdzono %d wzglednych linkow i obrazow, zepsutych %d" % (ile, len(zle)))
    for p, nr, cel in zle:
        print("  %s:%d -> %s" % (p, nr, cel))
    return 1 if zle else 0


if __name__ == "__main__":
    sys.exit(main())
