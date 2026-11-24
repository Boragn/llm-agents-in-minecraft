# Wiedza, menu akcji, percepcja i metapoznanie: co decyduje o skuteczności agenta LLM w świecie gry

*Esej inżynierski na podstawie historii zmian projektu agentów, które grają w Minecrafta przez tekstowy interfejs. Szkic, wersja 0.2, stan na 13 listopada 2026.*

## Streszczenie

W kilka dni, z zespołem agentów programujących, zbudowałem system, w którym modele językowe (Haiku, Sonnet, Opus) sterują dwiema postaciami w Minecrafcie: górnikiem Borysem i łowczynią Wilgą. Model nie widzi obrazu i nie naciska klawiszy. Dostaje tekst (stan ciała, mapy, pamięć, listę możliwych akcji) i wydaje polecenia celowe, które wykonuje mod serwerowy. Harness woła model, przesuwa czas świata i zapisuje każdą turę.

Esej opisuje cztery grupy technik i ich wpływ, pokazany na prawdziwych zapisach: wiedzę agentów (od przyrostowego dopisywania do jednej tabeli zasad i rdzenia krótszego o 46%), interfejs akcji (menu akcji, tryb ścisły, walidacja łańcucha przed wykonaniem, ETA z przedziałem), system percepcji (klatka, mapy 2D i 3D, pamięć ciała, gotowa klatka środowiska w każdym wywołaniu, prototyp projekcji 3D na 2D) oraz metapoznanie na dwóch poziomach: środowisko, które wie, kiedy samo zawodzi, i agent, który ma rozumieć interfejs bez objaśnienia.

Najwięcej uczą porażki. Gdy menu akcji nie miało drogi na rynek ani wyjęcia rzeczy ze skrzyni, nawet najdroższy model tylko trafnie opisywał luki, ale nie miał czym ich obejść. Gdy narzędzie zawiodło przy drzwiach, bot zaczął rozbierać własny dom. Pierwsza pełna pętla „zdobądź, idź, sprzedaj” udała się dopiero w przebiegu WY-8, z poprawionym menu i klatką środowiska w kontekście.

## Teza

O skuteczności agenta LLM w złożonym, zmiennym środowisku w dużej mierze decyduje to, co środowisko mu podaje i jak uczciwie mówi o sobie: wiedza w jednym miejscu, menu akcji zgodne z tym, co naprawdę da się wykonać, percepcja, która zamienia pamięć w decyzje, i środowisko, które zna własne błędy i pewność swoich odpowiedzi. Wybór modelu ma znaczenie, ale dopiero na tym fundamencie.

## Spis rozdziałów

**Część 1. Wiedza i interfejs akcji** ([czesc-1-wiedza-i-interfejs-akcji/](czesc-1-wiedza-i-interfejs-akcji/))

1. [Pytanie badawcze i metoda](czesc-1-wiedza-i-interfejs-akcji/01-pytanie-i-metoda.md)
2. [Środowisko: co zbudowano](czesc-1-wiedza-i-interfejs-akcji/02-srodowisko.md)
3. [Wiedza agentów: budowa i przetwarzanie](czesc-1-wiedza-i-interfejs-akcji/03-wiedza-agentow.md)
4. [Interfejs akcji](czesc-1-wiedza-i-interfejs-akcji/04-interfejs-akcji.md)

**Część 2. Percepcja i metapoznanie** ([czesc-2-percepcja-i-metapoznanie/](czesc-2-percepcja-i-metapoznanie/))

5. [System percepcji: jak ciało widzi świat](czesc-2-percepcja-i-metapoznanie/05-system-percepcji.md)
6. [Klatka środowiska w kontekście bota](czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md)
7. [Projekcja 3D na 2D: prototyp](czesc-2-percepcja-i-metapoznanie/07-projekcja-3d-na-2d.md)
8. [Metapoznanie: system o sobie i agent o systemie](czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md)
9. [Planowanie, metody obserwacji i kalibracja](czesc-2-percepcja-i-metapoznanie/09-planowanie-i-kalibracja.md)
10. [Pamięć: wspomnienia, epizody i sieć znaczeń](czesc-2-percepcja-i-metapoznanie/10-pamiec-wspomnienia-siec-znaczen.md)

**Dodatki:** [glosariusz pojęć i symboli klatki](dodatki/glosariusz.md), [protokół eksperymentu poziomu 2](dodatki/protokol-eksperymentu-poziom-2.md), [tor kontrolny](dodatki/tor-kontrolny.md), [surowe klatki ASCII](dodatki/klatki-surowe/), [dane do figur i tabel (CSV)](dodatki/dane/).

**Filmy** (GIF, [archiwum](dodatki/filmy/)): wplecione w tekst przy miejscach, które pokazują: Film 1 do 6 z przebiegu WY-8 w rozdziałach 5 do 10 (pliki w [dodatki/filmy/wy8/](dodatki/filmy/wy8/)), Film 7 do 9 z przebiegu WY-9 z paskiem i osią decyzji modelu w rozdziałach 8.1.5 i 9.2.

**Figury** ([figury/](figury/)): rys. 1a i 1b mapa 2D klatki, 2a i 2b mapa 3D klatki, 4b trajektoria Wilgi (rozdział 6); 3a i 3b porównanie rzutów (rozdział 7); 4a trajektoria Borysa i 5 oś czasu przebiegu (rozdział 8).

## Jak czytać

- Kto ma 10 minut: to README, potem [rozdział 4](czesc-1-wiedza-i-interfejs-akcji/04-interfejs-akcji.md) (dlaczego boty nie zarabiały) i [rozdział 8](czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md) (metapoznanie).
- Kto chce zobaczyć percepcję: [rozdział 5](czesc-2-percepcja-i-metapoznanie/05-system-percepcji.md) z rysunkami każdego odczytu ciała i [rozdział 6](czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) z figurami w kolorach przeglądarki przebiegów.
- Rozdziały pokazują dane jako rysunki w stylu przeglądarki przebiegów; surowy tekst (dokładnie to, co dostał model) jest w [dodatkach](dodatki/klatki-surowe/) i ma odnośnik „surowy zapis” pod każdym rysunkiem. Symbole wyjaśnia [glosariusz](dodatki/glosariusz.md).
- Każdy rozdział ma na górze streszczenie i odnośniki: poprzedni, indeks, następny.

## Status i zakres

- **Z żywych przebiegów:** przebiegi obserwacyjne WY-1 do WY-6 (audyty tur, koszty, błędy), odczyty zatrzymanych ciał po WY-6 (rozdział 5), klatki, dziennik, trajektorie i alarmy detektora z WY-8 (rozdziały 6 i 8, rys. 1, 2, 4, 5). WY-8 trwał w chwili pisania; liczby z niego są stanem z 13 listopada rano.
- **Z analiz offline i prototypów:** przetworzenie wiedzy (rozdział 3), rozrzut ETA z logów (rozdział 4), prototyp projekcji 3D na 2D liczony z kopii świata z pełną wiedzą (rozdział 7, rys. 3), detektor błędów sprawdzony wstecz na zapisach WY-5 do WY-7, stan zagrożeń sprawdzony testami i samotestem bez wdrożenia (rozdział 8).
- **Pamięć (rozdział 10):** inbox wspomnień, wyzwalacze, zatrzymanie świata, subagent tylko do odczytu, strażnik zapisu i warstwa lekcji zostały sprawdzone dry-runem na prawdziwych, płaskich wspomnieniach z WY-8. Schemat epizodu (encje, lokacja, rzut 2,5D z peaku, czynność poprzednia i następna, wynik, waga, pewność) i sieć znaczeń są projektem, niezaimplementowanym. Rysunki 10.1, 10.3 i 10.4 to wizualizacje danych z logów WY-8 zbudowane skryptem figur, a nie wyniki działającego systemu.
- **Filmy:** kadry są liczone offline z pamięci ciała, logu moda i kopii świata (sprzed przebiegu), więc ścięte drzewo w filmie Borysa jeszcze stoi; kierunek patrzenia jest odtworzony z ruchu i pola `patrzy` klatki. GIF jest animowany tylko w widoku repozytorium.
- **Jeszcze nie zrobione:** eksperyment poziomu 2 (czy agent sam rozumie klatkę) ma tylko protokół; eksploracja z kryterium sukcesu jest projektem. Rozdziały oznaczają to w tekście.
- Esej jest rekonstrukcją z historii zmian, nie eksperymentem kontrolowanym: dwa ciała, jedna mapa, kilka przebiegów.

## Budowanie wersji jednoplikowej

```sh
python3 -I narzedzia/zbuduj_calosc.py          # tworzy esej-calosc.md (README + rozdziały + glosariusz), sprawdza odnośniki
python3 -I narzedzia/sprawdz_odnosniki.py      # sam test względnych linków i obrazów
python3 -I narzedzia/tabele_csv.py             # tabele z rozdziałów do dodatki/dane/tabele/
python3 -I figury/figury.py --mp <katalog-projektu-gry>   # odtworzenie figur i danych do figur z zapisów
```

`esej-calosc.md` używa tych samych figur SVG (katalog `figury/` obok), więc nadaje się do konwersji na PDF narzędziem, które obsługuje SVG.

## Struktura katalogów

```
README.md                               ten indeks
czesc-1-wiedza-i-interfejs-akcji/       rozdziały 1-4
czesc-2-percepcja-i-metapoznanie/       rozdziały 5-10
figury/                                 figury SVG, generator figury.py, README
dodatki/                                glosariusz, protokoły, surowe klatki, dane CSV
narzedzia/                              zbuduj_calosc.py, sprawdz_odnosniki.py, tabele_csv.py
```

## Prywatność

Materiały źródłowe pochodzą z prywatnych repozytoriów. Wersja publiczna nie zawiera nazw klientów, nazwisk innych osób, adresów i nazw maszyn, ścieżek z dysku autora ani danych z poczty. Zostają współrzędne w grze i imiona postaci (Borys, Wilga, mieszkańcy wioski). Przed każdą publikacją całe drzewo, w tym pliki SVG i CSV, przechodzi skan prywatności, a lokalny katalog roboczy autora z listą źródeł nie wchodzi do repozytorium (zob. `.gitignore`).
