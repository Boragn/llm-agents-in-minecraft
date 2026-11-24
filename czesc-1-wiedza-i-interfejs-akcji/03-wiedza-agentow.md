# 3. Wiedza agentów: budowa i przetwarzanie

> Jak przyrostowo rosła wiedza botów, skąd wzięły się sprzeczności i co dało skrócenie rdzenia o 46%.

[← 2. Środowisko: co zbudowano](02-srodowisko.md) · [indeks](../esej-indeks.md) · [4. Interfejs akcji →](04-interfejs-akcji.md)

---

## 3.1 Przyrostowe dopisywanie i jego koszt

Wiedza botów to katalog plików Markdown: `CLAUDE.md` wczytywany automatycznie w każdym wywołaniu, plik roli, `strategia.md`, a obok kilkanaście plików tematycznych (polecenia, handel, przetrwanie, rudy, okolica startu). Przez trzy dni wiedza rosła przyrostowo: każdy audyt i każda nowa funkcja moda dopisywały akapit. Po piątym przebiegu katalog miał ok. 284 tys. znaków, a rdzeń czytany w każdym wywołaniu (`CLAUDE.md` + `strategia.md`) 16 411 znaków.

Przyrost miał trzy skutki uboczne, które wyszły dopiero przy systematycznym przeglądzie:

1. **Sprzeczności.** Znalazłem 24 sprzeczne albo nieaktualne wpisy. Przykład z jednego pliku: w wierszu 17 „tu NIE wolno kopać”, w wierszu 19 „kopanie wolno wszystkim”. Inny przykład: wiedza opisywała ciągły dzień, a reset ustawiał płynącą dobę; boty planowały pracę w polu w nocy.
2. **Duplikaty.** Zasady strefy ochronnej były w 6 miejscach, ceny handlarza w 4, zasada nocy w 5. Każda zmiana reguły aktualizowała część kopii.
3. **Wiedza nieczytana.** Kluczowe zdanie „ciało pije samo przy pragnieniu < 7” leżało w pliku tematycznym, którego w przebiegu WY-6 nie otworzył żaden bot (0 wywołań odczytu pliku w transkryptach). Wiedza, której model nie czyta, nie istnieje.

## 3.2 Przetworzenie: jedna tabela zasad, krótszy rdzeń

Przetworzenie wiedzy zrobiłem jako osobne zadanie: audyt każdego pliku z dowodem z kodu albo logu (plik i wiersz, „przed”, „po”, dowód), nowa wersja w osobnym katalogu, stara nietknięta do porównania.

| plik | przed (znaki) | po (znaki) | zmiana |
|---|---:|---:|---:|
| `CLAUDE.md` (czytany co wywołanie) | 13 297 | 6 537 | -51% |
| `strategia.md` | 3 114 | 2 332 | -25% |
| **rdzeń co wywołanie** | **16 411** | **8 869** | **-46%** |
| rdzeń + rola górnika | 19 596 | 10 830 | -45% |
| handel i NPC | 11 691 | 3 758 | -68% |
| tabela błędów i napraw (nowa) | 0 | 4 183 | nowa |
| cały katalog bez archiwum | 283 733 | 250 822 | -12% |

Najważniejsze zmiany:

- **Jedno źródło zasad.** Zasady operatora scalone w jedną tabelę z rozróżnieniem „KOD” (egzekwuje mod) i „ZASADA” (umowa, którą bot ma przestrzegać sam). `CLAUDE.md` ma tylko skrót i odsyłacz.
- **Tabela błędów.** Nowy plik: kod błędu, co znaczy, jak naprawić, zebrany z logów pięciu przebiegów. Przykładowy wiersz: `E_BRAK_STOLU (craft wooden_pickaxe)`: stół musi stać w 4 blokach, nie leżeć w ekwipunku; naprawa: `craft crafting_table ; postaw crafting_table ~1 ~0 ~0`, a kilof w następnym łańcuchu.
- **Role bez zakazów i bez poleceń.** Obie role mają te same sekcje w tej samej kolejności (fach, czego nie lubisz, z czym przychodzisz, czego pragniesz, jak zarabiasz, poza fachem). Zero komend i ścieżek: rola mówi „kim jesteś i czego chcesz”, a nie „co wpisać”.
- **Rzeczy krytyczne w rdzeniu.** Prompt trybu zdarzeniowego nie kazał czytać `strategia.md`, więc realnie co wywołanie ładował się tylko `CLAUDE.md`. Cel, ocena, sprzedaż, noc i zasady trafiły tam.

## 3.3 Wpływ

Wpływ jest mieszany i trzeba to powiedzieć wprost. W przebiegu WY-6 (pierwszym na nowej wiedzy) Opus najlepiej ze wszystkich modeli trzymał się zasad (odległość od dzwonu, cudze skrzynie, przerwanie na zagrożenie w każdym łańcuchu). Ale zarobek nie wzrósł, bo menu akcji nie pozwalało wykonać tego, co wiedza zalecała: `CLAUDE.md` kazał wyjąć zestaw startowy ze skrzyni, a menu trybu ścisłego nie miało akcji „wyjmij”. Wiedza i interfejs akcji rozjechały się, a rozjazd wiedzy z interfejsem jest gorszy niż brak wiedzy, bo model traci wywołania na próby.

---

[← 2. Środowisko: co zbudowano](02-srodowisko.md) · [indeks](../esej-indeks.md) · [4. Interfejs akcji →](04-interfejs-akcji.md)
