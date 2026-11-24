#!/usr/bin/env python3
"""Sklada wszystkie rozdzialy eseju w jeden plik esej-calosc.md (do PDF albo wysylki z CV), bez katalogu _prywatne.

Kroki: (1) README (bez sekcji o strukturze i budowaniu) + rozdzialy czesc-*/NN-*.md w kolejnosci numerow
+ glosariusz; (2) linki miedzy rozdzialami zamieniane na zwykly tekst, sciezki figur i dodatkow przepisane
wzgledem katalogu glownego; (3) sprawdzenie odnosnikow w wyniku; (4) skan prywatnosci, jesli jest dostepny
lokalnie (_prywatne/skan_prywatnosci.py; w repozytorium publicznym go nie ma i krok jest pomijany).

Uzycie: python3 -I narzedzia/zbuduj_calosc.py [--wyjscie esej-calosc.md]
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def wczytaj_rozdzial(p):
    t = p.read_text(encoding="utf-8")
    linie = [l for l in t.splitlines() if not re.match(r"^\[(← |indeks)", l)]
    t = "\n".join(linie)
    t = re.sub(r"\n---\n(\s*\n---\n)?", "\n", t)
    wyn, kod = [], False
    for l in t.splitlines():  # naglowki o jeden poziom nizej (rozdzial = ##), bez zmian w blokach kodu
        if l.strip().startswith("```"):
            kod = not kod
        wyn.append("#" + l if (not kod and re.match(r"^#+ ", l)) else l)
    t = "\n".join(wyn)
    # linki do innych rozdzialow -> sam tekst
    t = re.sub(r"(?<!!)\[([^\]]+)\]\((?:\.\./czesc-[^/]+/|)(\d\d-[a-z0-9-]+\.md)(#[^)]*)?\)", r"\1", t)
    t = t.replace("](../figury/", "](figury/").replace("](../dodatki/", "](dodatki/")
    return t.strip() + "\n"


def main():
    wyj = ROOT / (sys.argv[sys.argv.index("--wyjscie") + 1] if "--wyjscie" in sys.argv else "esej-calosc.md")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    czesci = re.split(r"(?m)^## ", readme)
    glowa = czesci[0].strip()
    zachowaj = [c for c in czesci[1:] if c.split("\n", 1)[0].strip().lower().startswith(("streszczenie", "teza", "status"))]
    out = [glowa, "", "> Uwaga: filmy (GIF) są animowane tylko w widoku repozytorium; w PDF albo wydruku widać pierwszą klatkę, a każdy film jest też linkiem do pliku.", ""] + ["## " + c.strip() + "\n" for c in zachowaj]
    rozdzialy = sorted(ROOT.glob("czesc-*/[0-9][0-9]-*.md"), key=lambda p: p.name)
    for p in rozdzialy:
        out.append(wczytaj_rozdzial(p))
    g = (ROOT / "dodatki" / "glosariusz.md").read_text(encoding="utf-8")
    g = "\n".join(l for l in g.splitlines() if not l.startswith("[indeks]"))
    g = g.replace("# Glosariusz", "## Aneks: glosariusz", 1).replace("](../czesc-2-percepcja-i-metapoznanie/", "](czesc-2-percepcja-i-metapoznanie/")
    g = re.sub(r"(?m)^## (?!Aneks)", "### ", g)
    out.append(g)
    tekst = "\n".join(out)
    tekst = re.sub(r"(?<!\[)!\[([^\]]*)\]\(([^)]+\.gif)\)", r"[![\1](\2)](\2)", tekst)
    tekst = re.sub(r"\n{3,}", "\n\n", tekst)
    wyj.write_text(tekst, encoding="utf-8")
    print("ZBUDOWANO %s: %d rozdzialow, %d slow" % (wyj.name, len(rozdzialy), len(tekst.split())))
    kod = subprocess.call([sys.executable, "-I", str(ROOT / "narzedzia" / "sprawdz_odnosniki.py"), str(ROOT)])
    skan = ROOT / "_prywatne" / "skan_prywatnosci.py"
    if skan.exists():
        kod |= subprocess.call([sys.executable, "-I", str(skan), str(ROOT)], stdout=subprocess.DEVNULL) and 2
        print("SKAN PRYWATNOSCI: %s" % ("OK, 0 trafien" if not kod & 2 else "SA TRAFIENIA, uruchom skan recznie"))
    else:
        print("SKAN PRYWATNOSCI: pominiety (brak _prywatne/skan_prywatnosci.py w tej kopii)")
    return 1 if kod else 0


if __name__ == "__main__":
    sys.exit(main())
