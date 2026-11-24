# Filmy percepcji agenta

[artykuł](../../README.pl.md) · [article (EN)](../../README.md) · [dodatki](../README.md) · archiwum filmów; w artykule są osadzone Film 7 (Borys, sekcja 4) i Film 4 (Wilga, sekcja 5)

Krótkie filmy ze świata gry tak, jak widzi go ciało bota: widok z oczu, rzut 2,5D i jego pochodne (mapa 2D, warstwy 3D, radar), ekwipunek, wyposażenie, rola, a od WY-9 także pasek decyzji modelu i oś decyzji całego przebiegu. GIF jest formatem głównym (odtwarza się w podglądzie GitHuba i na każdym hoście; MP4 z H.264 nie na każdym).

## Filmy WY-9 (kroki 1-11, główne)

Przebieg WY-9: 11 kroków po 150 ticków (ticki 1851520 … 1853170), model Sonnet, 12 wywołań (Borys 7, Wilga 5), klatka środowiska z widokiem 2,5D w prompcie, menu akcji w trybie ścisłym (`wykonaj A<n>`).

| film | ciało | ticki | czas | GIF | klatka kontrolna |
|---|---|---|---|---|---|
| Film 7. Eksploracja lasu z celem (A26) kończy się `E_NIE_ZNALEZIONO`, potem dryf w polowanie (A72 kura, A69 owca dwa razy) | Borys (górnik) | 1851670 … 1853020 | 26 s | [wy9-borys-eksploracja-i-polowanie.gif](wy9-borys-eksploracja-i-polowanie.gif) | [png](klatka-kontrolna-wy9-borys-eksploracja-i-polowanie.png) |
| Film 8. Eksploracja zwierzyny (A25), błąd kroku `E_BRAK_DROGI`, „idź do kury” (A2) w kolejce za eksploracją, potem `E_NIE_ZNALEZIONO` i `E_BRAK_CELU`; polowania nie było | Wilga (łowczyni) | 1851670 … 1852940 | 24 s | [wy9-wilga-eksploracja-zwierzyny.gif](wy9-wilga-eksploracja-zwierzyny.gif) | [png](klatka-kontrolna-wy9-wilga-eksploracja-zwierzyny.png) |
| Film 9. Para w kroku 11: Borys A71 + A68 (łańcuch przerwany `E_BRAK_CELU` na kroku 2), Wilga A19 (krok 1/2 zrobiony, łańcuch niedokończony na końcu danych) | Borys i Wilga | 1853020 … 1853170 | 16 s | [wy9-para-krok-11.gif](wy9-para-krok-11.gif) | [png](klatka-kontrolna-wy9-para-krok-11.png) |

Każdy GIF ma do ok. 3 MB.

### Pasek decyzji i oś decyzji (nowe w WY-9)

| miejsce | co pokazuje |
|---|---|
| **pasek DECYZJA MODELU** (pod kafelkami) | ostatnie wywołanie modelu do bieżącego ticku: numer i tick wywołania, wyzwalacz (koniec łańcucha, odkrycie, błąd) i błąd kroku z dziennika; `PLAN:` w jednej linii (w filmie pary w dwóch) z odpowiedzi modelu; **wybór z menu**: `A<n>`, kategoria i polecenie tej pozycji z listy `akcje` tej tury; **wynik**: łańcuch `k-NNN` i jego stan w bieżącym ticku (w kolejce za innym łańcuchem, trwa krok i/n, ZROBIONE, kod błędu z opisem, NIEDOKOŃCZONY na końcu danych). W chwili wywołania film zatrzymuje się na 1 s, a pasek dostaje żółtą ramkę |
| **oś decyzji** (pasek czasu na dole) | cały przebieg WY-9, nie tylko fragment filmu (jaśniejsze pole = fragment); ▼ każde wywołanie modelu z etykietą `nr:A<n>` (`dalej` = wywołanie bez nowego wyboru, model kontynuuje) w kolorze wyniku: zielony zrobione, czerwony błąd, żółty trwa albo niedokończony, szary bez wyboru; pasy kroków łańcuchów w kolorach kategorii, krok zakończony błędem w czerwonej ramce ze znakiem x; ▲ kulminacje (zabicie, błąd) |

Pasek i oś biorą dane tylko z dziennika przebiegu (`PLAN`, polecenie, wyzwalacze, błędy), z transkryptów tur (lista `akcje`, z której pochodzi opis `A<n>`) i z logu moda (przyjęcie łańcucha, liczba kroków, wynik każdego kroku). Nic nie jest dopowiadane. W audycie WY-9 modele przed każdym wyborem wołały `akcje` i wybierały pozycję z menu; ich krótkie uzasadnienia nie odwołują się do rysunku mapy, a liczby w planach (np. „cel 36 m SW”, współrzędne kury) pochodzą z tekstowych linii klatki (TRASA) i z odpowiedzi `wykonaj` (symulacja). Filmy pokazują więc, co ciało mogło wiedzieć w chwili wyboru, obok tego, co model wybrał; nie pokazują, że rzut 2,5D w prompcie poprawił decyzje.

### Kadr filmu pary (Film 9)

Lewa połowa Borys, prawa Wilga, ten sam tick. Każde ciało: widok z oczu D (624x351, ok. 1/4 kadru), rzut 2,5D w mniejszej skali z nakładkami A, B, C, D, kafelki EKWIPUNEK, WYPOSAŻENIE (ręka i paski) i ROLA oraz własny pasek decyzji. Na dole wspólna oś decyzji w dwóch pasach (Borys, Wilga). Osobnych paneli A, B i C nie ma (są jako nakładki na 2,5D).

## Filmy WY-8 (archiwum, katalog [wy8/](wy8/))

Świat sprzed przebiegu WY-9, bez widoku 2,5D w prompcie modelu i bez paska decyzji (pasek dodany później; generator z obecnym kodem dorysowałby go, ale klatki percepcji ciał z WY-8 zostały nadpisane po restarcie serwera, więc filmów WY-8 nie odtwarzamy ponownie).

| film | ciało | ticki | czas | GIF | MP4 |
|---|---|---|---|---|---|
| (a) polowanie na krowę, zabicie, droga na rynek i sprzedaż | Wilga (łowczyni) | 1848500 … 1849520 | 22 s | [wilga-polowanie-i-sprzedaz.gif](wy8/wilga-polowanie-i-sprzedaz.gif) | [mp4](wy8/wilga-polowanie-i-sprzedaz.mp4) |
| (b) marsz na zachód, ścięcie całego drzewa, craft stołu | Borys (górnik) | 1848317 … 1850400 | 25 s | [borys-eksploracja-i-drzewo.gif](wy8/borys-eksploracja-i-drzewo.gif) | [mp4](wy8/borys-eksploracja-i-drzewo.mp4) |
| (c) wszystkie przekroje w jednym miejscu, obrót kamery | Borys w domku | 1848167 | 16 s | [borys-przekroje-domek.gif](wy8/borys-przekroje-domek.gif) | [mp4](wy8/borys-przekroje-domek.mp4) |

### Numeracja filmów

| film | plik | w artykule |
|---|---|---|
| Film 1 | [wy8/borys-przekroje-domek.gif](wy8/borys-przekroje-domek.gif) | |
| Film 2 | [wy8/klip-borys-2d-25d-3d.gif](wy8/klip-borys-2d-25d-3d.gif) (klip 9 s) | |
| Film 3 | [wy8/borys-eksploracja-i-drzewo.gif](wy8/borys-eksploracja-i-drzewo.gif) | |
| Film 4 | [wy8/wilga-polowanie-i-sprzedaz.gif](wy8/wilga-polowanie-i-sprzedaz.gif) | sekcja 5 (monitoring) |
| Film 5 | [wy8/klip-wilga-oczy-mgla.gif](wy8/klip-wilga-oczy-mgla.gif) (klip 8 s) | |
| Film 6 | [wy8/klip-borys-radar-25d.gif](wy8/klip-borys-radar-25d.gif) (klip 8 s) | |
| Film 7 | [wy9-borys-eksploracja-i-polowanie.gif](wy9-borys-eksploracja-i-polowanie.gif) | sekcja 4 (planowanie) |
| Film 8 | [wy9-wilga-eksploracja-zwierzyny.gif](wy9-wilga-eksploracja-zwierzyny.gif) | |
| Film 9 | [wy9-para-krok-11.gif](wy9-para-krok-11.gif) | |

Klatka kontrolna WY-8 (widok z oczu ograniczony percepcją, mgła nieznanego): [wy8/klatka-kontrolna-wilga.png](wy8/klatka-kontrolna-wilga.png).
Migawka danych WY-8: log ciał do ticku 1850460, pamięć ciał zapisana do ticku 1849300. Migawka WY-9: log ciał do ticku 1853170, pamięć ciał zapisana do ticku 1852860.

## Układ kadru (1280x784, GIF do 1000 px)

Ten sam schemat co figury: **2,5D jest widokiem bazowym agenta**, a pozostałe widoki są jego pochodnymi, oznaczonymi literą źródła i miniaturą 2,5D z podświetloną częścią, z której pochodzą.

| miejsce | co pokazuje |
|---|---|
| **D** lewa górna ćwiartka (640x360, ok. 1/4 kadru) | widok z oczu ciała: perspektywa, kąt 70°, zasięg 20 m (promień percepcji); tylko komórki, które ciało zna; kratka = nieznane (mgła), jasna mgła = odległość i to, co poza zasięgiem; zwierzęta, NPC i drugie ciało jako prostokąty z nazwą i odległością, zasłonięte nie są rysowane |
| **2,5D** prawa górna ćwiartka | rzut izometryczny otoczenia w promieniu 11 m (kamera od SW jak w figurach; w filmie obrotowym obraca się), z nakładkami: A płyta mapy 2D, B prostopadłościan warstw, C promienie radaru na podłożu, D stożek wzroku; etykiety „nazwa, 12 m SW, +3 w górę” |
| **A** | mapa 2D z góry, r 24 m, ślad ciała, byty, kierunek patrzenia |
| **B** | sześć warstw 3D y-2 … y+3 wokół stóp, r 6 m |
| **C** | radar 16 promieni do 12 m (wolne, drzwi, przeszkoda, spadek, nieznane) i lista afordancji z wiedzy ciała z kierunkiem i odległością |
| EKWIPUNEK | przedmioty i liczby; zielona ramka = przybyło w ostatnich 3 s, czerwony napis = ubyło |
| WYPOSAŻENIE | co w ręce, co założone (zbroja, tarcza), narzędzia pod ręką, paski hp, głodu i staminy |
| ROLA | kim jest i czego chce (z pliku roli) oraz aktualny `PLAN:` z dziennika modelu |
| DECYZJA MODELU | pasek decyzji (opis wyżej) |
| oś czasu | tick, czas gry od początku fragmentu, akcja z menu (`wykonaj A26 → eksploruj las`), ETA z walidacji łańcucha, oś decyzji (opis wyżej) |

**Rzut z peaku.** W kulminacji zdarzenia (zabicie, sprzedaż, zakup, ścięcie drzewa, craft, błąd) film zatrzymuje się na 1,5 s, a na rzucie 2,5D (w filmie pary: na widoku z oczu tego ciała) pojawia się ramka „RZUT Z PEAKU” w układzie komendy `klatka --skrot`: stan, afordancje, ekwipunek, najbliższe obiekty z kierunkiem i odległością. Skrót w filmie jest liczony offline z tych samych danych (wiedza ciała, ekwipunek, byty, miejsca).

## Jak powstały

Generator filmów nie jest publikowany (czyta prywatne zapisy przebiegów i kopię świata). Wymagał Pythona 3 z Pillow, `ffmpeg` (GIF z paletą z różnic klatek; MP4 przez `libopenh264`, a gdy to tylko zaślepka, VP9 w kontenerze MP4), czcionek Liberation. Bez numpy. Kadr liczy się ok. 0,2 s (para 0,4 s); powtórzone klatki zatrzymań liczą się raz. GIF dostaje mniej kolorów i mniejszą szerokość, aż zmieści się w limicie (WY-9: 3 MB). Wynik nie ma metadanych (`-map_metadata -1`, `+bitexact`). Generator tylko czyta dane; nie dotyka serwera, ciał ani świata.

## Źródła danych (tylko odczyt, katalog projektu gry)

| dane | skąd |
|---|---|
| bloki świata | kopia zapasowa świata sprzed przebiegu (WY-8: 13.11 rano, WY-9: 13.11, 2 min przed startem), parser Anvil z prototypu projekcji, nigdy żywy świat |
| co ciało wie | pamięć ciała `pamiec/mapa.txt` (komórka i tick ostatniego widzenia), `miejsca.json` |
| pozycje, ręka, hp, stamina, ekwipunek, łańcuchy (przyjęcie, liczba kroków, wynik każdego kroku), ETA, `patrzy=` | log moda ciała `mod.jsonl` |
| zwierzęta i NPC | sekcja BYTY klatek percepcji ciała (plik użyty tylko, gdy tick w nagłówku zgadza się z logiem) |
| rundy, wywołania modelu, PLAN, wyzwalacze, błędy kroku, polecenia `wykonaj`, opis pozycji menu | przebieg WY-8 albo WY-9: `rundy.jsonl`, `dziennik.jsonl`, `tury/*.jsonl`, `klatki/*.txt` |
| kim jest, czego chce | pliki ról górnika i łowczyni |
| paleta, nazwy miejsc po polsku, kierunki, łańcuchy | generator figur (niepublikowany) |

## Metoda i ograniczenia

- **Wiedza w ticku t.** Komórka jest znana, gdy pamięć ciała widziała ją najpóźniej w t, albo gdy jej kolumna leży w promieniu percepcji (20 m) od śladu ciała do t (rekonstrukcja pierwszego widzenia, jak w przeglądarce przebiegów; pamięć trzyma tylko ostatnie widzenie). Blok bierzemy z pamięci, gdy był widziany najpóźniej w t, inaczej z kopii świata. Po ticku zapisu pamięci wiedza o nowych miejscach to już tylko rekonstrukcja ze śladu, co kadr podaje w prawym górnym rogu.
- **Kierunek patrzenia.** Log moda nie zapisuje yaw ani pitch. Kierunek to kierunek ruchu (przemieszczenie > 0,3 m w oknie 12 ticków), w ataku i handlu kierunek na najbliższy cel, w bezruchu ostatni kierunek albo `patrzy=` z klatki percepcji; pitch stały -6°.
- **Zmiany świata.** Kopia świata jest sprzed przebiegu, więc zmiany zrobione w trakcie (ścięte drzewo w WY-8) widać dopiero, gdy pamięć ciała je zapisała. Ekwipunek pokazuje ubytek dopiero po kolejnym odpytaniu `ekwipunek`.
- **Byty** są z ostatniej klatki percepcji ciała (w WY-9 jedna na krok, co 150 ticków, do 20 s wstecz), więc poruszają się skokami albo znikają między klatkami; zabite zwierzę znika w ticku zabicia. Gracze-ludzie nie są pokazywani.
- **Widok z oczu** to raycasting 160x90 skalowany 4x, bez tekstur i oświetlenia: kolory jak w palecie figur, cieniowanie ścian i mgła odległości. Drzwi i szyby są pełnymi blokami, liście nieprzezroczyste.
- **Stan łańcucha** w pasku decyzji jest liczony z logu moda w bieżącym ticku; łańcuch bez końca w danych jest na końcu filmu oznaczony jako NIEDOKOŃCZONY.
- **Rzut z peaku** jest liczony offline w układzie `klatka --skrot`, nie odczytany z moda.

Kadry nie zawierają ścieżek plików, nazw hostów ani adresów; tylko imiona botów, współrzędne gry, identyfikatory pozycji menu i łańcuchów oraz liczby.
