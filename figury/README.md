# Figury

[indeks](../esej-indeks.md)

Figury SVG wygenerowane z prawdziwych zapisów skryptem figury.py (skrypt niepublikowany) (Python 3, tylko biblioteka standardowa). Paleta i znaczniki jak w przeglądarce przebiegów operatora: kolory terenu (`G` trawa, `L` las, `W` woda, `S` skała, `D` droga, `Z` zabudowa), Borys żółty, Wilga niebieska, trasa niebieska, cel czerwony, ślad fioletowy, miejsca z pamięci złote. Tło jest jednolite i ciemne, więc figury wyglądają tak samo w jasnym i ciemnym motywie GitHub.

| plik | rysunek | dane źródłowe | rodzaj | rozdział |
|---|---|---|---|---|
| `f1a-klatka2d-borys-wy8.svg` | 1a: mapa 2D klatki Borysa | WY-8, klatka tury 11 | żywy przebieg | [6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) |
| `f1b-klatka2d-wilga-wy8.svg` | 1b: mapa 2D klatki Wilgi | WY-8, klatka tury 14 | żywy przebieg | [6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) |
| `f2a-klatka3d-borys-wy8.svg` | 2a: mapa 3D, 6 warstw, Borys w domku | WY-8, klatka tury 1 | żywy przebieg | [6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) |
| `f2b-klatka3d-wilga-wy8.svg` | 2b: mapa 3D, 6 warstw, Wilga przy rynku | WY-8, klatka tury 14 | żywy przebieg | [6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) |
| `f3a-projekcja-domek.svg` | 3a: cztery rzuty danych i rzut wizualny 2,5D (izometryczny), domek Borysa na palach | prototyp projekcji, `domek-wnetrze` | prototyp offline (pełna wiedza) | [7](../czesc-2-percepcja-i-metapoznanie/07-projekcja-3d-na-2d.md) |
| `f3b-projekcja-mur-horda.svg` | 3b: cztery rzuty danych i rzut wizualny 2,5D, mur, horda i droga zombie | prototyp projekcji, `mur-horda` | prototyp, scenariusz syntetyczny | [7](../czesc-2-percepcja-i-metapoznanie/07-projekcja-3d-na-2d.md) |
| `f4a-trajektoria-borys-wy8.svg` | 4a: trajektoria Borysa z akcjami | WY-8, linie `stan` i wyniki kroków w dzienniku ciała | żywy przebieg | [8](../czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md) |
| `f4b-trajektoria-wilga-wy8.svg` | 4b: trajektoria Wilgi z akcjami | jak wyżej, łowczyni | żywy przebieg | [6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) |
| `f5-os-czasu-wy8.svg` | 5: oś ticków z akcjami (pasy ciał, kroki łańcuchów wg kategorii, bezczynność, wywołania modelu, zdarzenia, szmaragdy) | WY-8, dzienniki ciał (PRZYJETO, ZROBIONE, BLAD, PRZERWANY), `rundy.jsonl`, alarmy detektora, polecenia z klatek i menu tur; migawka do ticku 1850460 | żywy przebieg | [8](../czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md) |

| `p4-01-odpowiedzi-interfejsu.svg` | 4.1: pozycja menu, walidacja, okno czasu (karty) | formaty z opisu menu i specyfikacji okna | przykłady | [4](../czesc-1-wiedza-i-interfejs-akcji/04-interfejs-akcji.md) |
| `p5-01-stan-i-klatka.svg` .. `p5-11-przeplyw-percepcji.svg` | 5.1 do 5.11: STAN i klatka, mapa 2D, przekroje 3D, pokrycie i regiony, siatka osiągalności, eksploracja, pamięć na mapie, warstwy pamięci, przejęcie dropu, menu i walidacja, przepływ percepcji | `dodatki/klatki-surowe/odczyty/` (odczyty po WY-6, fragmenty WY-5 i WY-6), kopia świata (5.5) | żywe przebiegi i odczyty, 5.5 prototyp | [5](../czesc-2-percepcja-i-metapoznanie/05-system-percepcji.md) |
| `p6-01-sprzedaz-wy8.svg` | 6.1: pierwsza sprzedaż w WY-8 | dziennik tur 8 i 10 Wilgi | żywy przebieg | [6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) |
| `p8-01-stan-zagrozen.svg` | 8.1: stan zagrożeń z buforem | przykłady samotestu moda | test, bez wdrożenia | [8](../czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md) |

| `p10-01-anatomia-epizodu.svg` | 10.1: anatomia epizodu (sprzedaż Wilgi) | dziennik ciała WY-8, pamięć miejsc, kopia świata | dane z logów, schemat to projekt | [10](../czesc-2-percepcja-i-metapoznanie/10-pamiec-wspomnienia-siec-znaczen.md) |
| `p10-02-przeplyw-konsolidacji.svg` | 10.2: przepływ konsolidacji | moduł konsolidacji, dziennik dry-runu | schemat | [10](../czesc-2-percepcja-i-metapoznanie/10-pamiec-wspomnienia-siec-znaczen.md) |
| `p10-04-os-czasu-wspomnien.svg` | 10.3: oś czasu wspomnień z progami D i E | wspomnienia odtworzone funkcją konsolidacji na kopii WY-8 | symulacja na danych z logów | [10](../czesc-2-percepcja-i-metapoznanie/10-pamiec-wspomnienia-siec-znaczen.md) |
| `p10-03-siec-znaczen-wy8.svg` | 10.4: sieć znaczeń Wilgi i Borysa | jak wyżej plus pamięć miejsc | dane z logów, sieć to projekt | [10](../czesc-2-percepcja-i-metapoznanie/10-pamiec-wspomnienia-siec-znaczen.md) |
| `p10-05-dry-run-epizod.svg` | 10.5: dry-run: płaskie wspomnienie kontra epizod | `dodatki/dane/dry-run-konsolidacji/` | wynik próby (lewa), projekt (prawa) | [10](../czesc-2-percepcja-i-metapoznanie/10-pamiec-wspomnienia-siec-znaczen.md) |

| `p11-01-drzewo-wilga-wy8.svg` | Drzewo 1: decyzje Wilgi, WY-8 tury 7-12 | transkrypty tur (menu `akcje`, polecenia, thinking, koszt), dziennik, log ciała | żywy przebieg | [6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md) |
| `p11-02-drzewo-borys-wy8.svg` | Drzewo 2: decyzje Borysa, WY-8 tury 3-17 | jak wyżej, rundy bez wywołania z `rundy.jsonl` | żywy przebieg | [8](../czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md) |
| `p11-03-drzewo-borys-wy7-domek.svg` | Drzewo 3: Borys w domku, WY-7 tury 1-8, i wariant po naprawie (WY-8 tura 1) | transkrypty tur WY-7 i WY-8 (log moda WY-7 przepadł) | żywe przebiegi | [7](../czesc-2-percepcja-i-metapoznanie/07-projekcja-3d-na-2d.md) |

## Filmy

Filmy (GIF) leżą w [dodatki/filmy/](../dodatki/filmy/) (WY-9, Film 7 do 9) i [dodatki/filmy/wy8/](../dodatki/filmy/wy8/) (WY-8, Film 1 do 6) i są wplecione w tekst (lista osadzeń w README filmów). Generator: filmy.py (skrypt niepublikowany) (`--wy9` filmy WY-9 z paskiem i osią decyzji, GIF do 3 MB, `--wszystkie` filmy WY-8, `--klipy` krótkie klipy WY-8 pojedynczych przekrojów do 3 MB). Kadr ma ten sam schemat co figury: 2,5D jako widok bazowy i pochodne A do D z miniaturą i literą.

## Konwencja figur

- **Widok bazowy 2,5D.** Rzut izometryczny (panel e w rys. 3a i 3b) jest układem odniesienia. Kamera od południowego zachodu patrzy na NE: na ekranie N jest w górę w lewo, E w górę w prawo; róża kompasu w rogu jest liczona z tej samej projekcji i ma podpis „widok od SW”.
- **Odległości i kierunki.** Odległość jest pozioma, w blokach, czyli w metrach (1 blok = 1 m), liczona od ciała (@ = 0); wysokość podaje się osobno („+1 w górę”, „-3 w dół”). Kierunek to jeden z 8 (N, NE, E, SE, S, SW, W, NW), liczony od ciała. Etykiety obiektów mają postać „drzwi, 3 m SW” albo „piec, 1 m NE, +1 w górę”, zgodną z listą afordancji. W 2,5D osie wzdłuż przednich krawędzi podłoża mają podziałkę co 2 m (domek) albo 4 m (mur), pierścienie 4, 8 i 12 m leżą na podłożu, a pasek skali ma 4 m.
- **Nazwy.** Nazwy techniczne z pamięci ciała i konfiguracji wioski są zamieniane na polskie (np. `domek-kupca` = domek Borysa, `handel-handlarz` = Handlarz, `auto-skrzynia-5` = skrzynia 5, `kuznia` = kuźnia). Złote etykiety: pamięć ciała; białe: miejsca wioski. Etykiety mają linię odnoszącą i ciemne tło i omijają ciało oraz inne etykiety.
- **Radar w 2,5D.** 16 promieni co 22,5 stopnia z ciała na wysokości stóp, każdy kończy się przy pierwszym zdarzeniu: zielony wolne do zasięgu (12 m), niebieski drzwi, czerwony przeszkoda (ściana, szyba, mur), żółty spadek o 2 i więcej; etykieta przy końcu podaje odległość. Strzałka biała pokazuje kierunek patrzenia (yaw); w 3b czerwona strzałka pokazuje kierunek nadejścia hordy, a etykieta drogę zombie do bota.
- **Skąd pochodzą widoki (litery A, B, C, D).** Każdy widok jest pochodną widoku 2,5D i ma stały kolor i literę: **A** mapa 2D z góry (rzut z góry podłoża; także zmienna rozdzielczość i przejezdność), **B** warstwy i przekroje 3D (przekrój poziomy na y i pionowy wzdłuż osi przez ciało), **C** radar (promienie od @), **D** widok z oczu (pierwsza osoba, stożek widzenia 70 stopni). W 2,5D nakładki pokazują geometrię źródła (kwadrat podłoża A, prostopadłościan warstw B z linią cięcia, promienie C, stożek D); w pozostałych figurach miniatura 2,5D w rogu z literą, strzałką „z 2,5D” i podpisem, jak widok powstał.
- **Filmy.** Filmy stosują ten sam schemat: w kadrze miniatura 2,5D w rogu z podświetlonym źródłem, litera A do D w tym samym kolorze, róża kompasu zgodna z kamerą, odległości w metrach od @.
- **Czytelność.** Tekst ma co najmniej 11 px przy szerokości 1000 px (figury 3a i 3b mają szerokość 1000 px), tło jest jednolite i ciemne, rysunki są wektorowe.

## Uruchomienie

```sh
python3 -I figury.py --mp <katalog-projektu-gry> [--wyjscie .] [--dane ../dodatki/dane]
# opcjonalnie inne klatki: --borys 011-kupiec.txt --borys3d 001-kupiec.txt --wilga 014-lucznik.txt
```

`<katalog-projektu-gry>` to katalog z zapisami przebiegów (`scenariusze/obserwacja/wy8`), prototypem projekcji (`projekcja/przyklady`) i dziennikami ciał. Bez argumentu skrypt szuka go obok katalogu eseju. Skrypt zapisuje też liczby użyte w figurach do `dodatki/dane/` (CSV). Do figur nie trafiają ścieżki plików ani nazwy maszyn, tylko współrzędne gry, imiona postaci i liczby.

Rzut izometryczny (panel e w rys. 3) liczy funkcja `rzut_izo`: bloki z prototypu projekcji (kopia świata tylko do odczytu albo scenariusz syntetyczny) jako sześciany z trzema widocznymi ścianami (góra jasna, ściany W i S ciemniejsze), kamera od południowego zachodu, wielokąty wektorowe bez wstawek rastrowych; półpłytki i schody są uproszczone do pełnych bloków, roślinność pominięta, w domku zdjęty dach nad głową ciała.

Ograniczenia: trajektorie pomijają skoki pozycji dłuższe niż 60 bloków (teleport przy resecie albo przerwa w zapisie); tło trajektorii to wiedza ciała z ostatniej klatki, nie cały świat; radar w rys. 3 ma skalę pierwiastkową, żeby bliskie przeszkody były widoczne.
