# Glosariusz: pojęcia i symbole klatki

[indeks](../esej-indeks.md) · [dodatki](README.md)

## Pojęcia

- **Ciało:** postać sterowana przez agenta (bot-NPC na serwerze), z ekwipunkiem, wytrzymałością, pragnieniem.
- **Łańcuch:** lista do 5 kroków poleceń wykonywana przez mod bez wołania modelu.
- **Tick (t):** jednostka czasu gry, 20 t = 1 s.
- **Tryb ścisły:** model może wykonać tylko akcje z menu (`wykonaj A<n>`).
- **Tryb zdarzeniowy:** świat idzie krokami po 150 t, model jest wołany tylko przy wyzwalaczu.
- **Wywołanie produktywne:** wywołanie modelu, po którym w świecie przybyło przedmiotu, craftu albo odkrycia.
- **Harness:** skrypt, który woła model, przesuwa świat, czyta logi i zapisuje dziennik przebiegu.
- **Klatka percepcji:** tekst, który ciało zwraca na `percepcja` (STAN, STRESZCZENIE, SIATKA, BYTY, ZDARZENIA), opisany w [rozdziale 5](../czesc-2-percepcja-i-metapoznanie/05-system-percepcji.md).
- **Klatka środowiska:** gotowy tekst wkładany przez harness do każdego wywołania (STAN, mapa 3D, mapa 2D, miejsca, trasa, ślad), opisany w [rozdziale 6](../czesc-2-percepcja-i-metapoznanie/06-klatka-srodowiska.md).
- **Afordancja:** to, co ciało może zrobić z danym miejscem albo obiektem (wejdziesz, zejdziesz, otworzysz, dojdą), opisana wprost w tekście.
- **Metapoznanie, poziom 1, 2, 3:** system o sobie, agent o systemie, bot o własnym planie ([rozdział 8](../czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md)).

## Mapa 3D klatki (warstwy y+3 .. y-2)

| znak | znaczenie | znak | znaczenie |
|---|---|---|---|
| `#` | lity blok | `.` | powietrze albo roślina |
| `~` | woda | `^` | lawa |
| `o` | ruda | `L` | drzewo (pień, liście) |
| `z` | zabudowa | `H` | drabina |
| `/` | drzwi | `c` | skrzynia albo beczka |
| `t` | stół rzemieślniczy | `f` | piec |
| `b` | łóżko | `\|` | płot, mur, krata |
| `?` | nieznane | `@` / `&` | ciało / drugi bot |

## Mapa 2D klatki (widok z góry)

Teren: `G` trawa, `L` las, `W` woda, `S` skała, `P` piasek, `D` droga, `Z` zabudowa, `F` pole, `N` śnieg, `V` lawa, `X` inne, `?` nieznane (mgła), `-` widziane bez pewnej powierzchni. Wielka litera = widziane w ostatnich 60 s, mała = starsze.

Znaczniki: `@` ciało, `&` drugi bot, `T` cel łańcucha, `*` trasa łańcucha, `1`..`9` ślad poprzednich klatek, `A B C E H I J K M O Q R U Y` miejsca z pamięci, `a` stado, `o` złoże rudy, `m` wrogie moby, `:` granica strefy wioski, `!` granica obszaru gry.

## Prototyp projekcji: przejezdność 2,5D

`@` ty, `.` Twój poziom, `1`..`9` wyżej o tyle bloków (1 = skok, 2 = wspinaczka), `a`..`i` niżej o 1..9 (do `c` zejdziesz), `/` drzwi drewniane, `=` furtka, `H` drabina, `~` woda, `K` skrzynia. Nieprzejezdne: `#` ściana albo uskok > 2, `|` płot lub mur 1,5, `v` spadek >= 4, `^` lawa lub ogień, `I` żelazne drzwi, `x` odcięte, `m` wróg.

## Prototyp projekcji: radar kątowy

32 promienie co 11,25 stopnia (0 = N), komórka = typ i odległość w metrach: `z` ściana, `#` skała, `L` pień, `l` liście, `g` szyba, `|` płot, `/` drzwi, `=` furtka, `H` drabina, `K` skrzynia, `f` piec, `t` stół, `b` łóżko, `~` woda, `^` lawa, `!` ogień; `.` nic do 32 m.

## Kolory figur

Figury używają palety przeglądarki przebiegów: teren jak `EKKOL` (trawa `#6f9a52`, las `#2f6b3a`, woda `#3f78b8`, skała `#8a8f98`, piasek `#d8c690`, droga `#a88a5a`, zabudowa `#b0603a`, pole `#b5a63c`), Borys `#ffd36b`, Wilga `#4fb3d9`, trasa `#4fb3d9`, cel `#e5565b`, ślad `#b48ead`, miejsca `#e8d06b`; tło `#0f1218`.

## Konwencja figur i skąd pochodzą widoki

- **Widok 2,5D jako układ odniesienia.** Rzut izometryczny od SW (N w górę w lewo, E w górę w prawo) jest widokiem bazowym; pozostałe widoki są jego pochodnymi.
- **Litery źródeł:** A mapa 2D z góry (także przejezdność i zmienna rozdzielczość), B warstwy i przekroje 3D, C radar (promienie od @), D widok z oczu (pierwsza osoba). Ta sama litera i kolor w nakładce 2,5D, w miniaturze w rogu innych figur i w legendzie; ten sam schemat stosują filmy.
- **Odległość i kierunek:** poziomo w metrach (1 blok = 1 m) od ciała (@ = 0), kierunek jeden z 8, wysokość osobno („+2 w górę”). Przykład etykiety: „kuźnia, 33 m SE”, „drzwi, 3 m SW”.
- **Radar w 2,5D:** zielony wolne, niebieski drzwi lub przejście, czerwony przeszkoda, żółty spadek; liczba przy końcu promienia to odległość w metrach.
- **Nazwy miejsc:** polskie odpowiedniki nazw technicznych (domek Borysa, domek Wilgi, skrzynia domku, Handlarz, Stajenny, Strażnik Bramy, kuźnia, studnia, rynek, koszary, ratusz, gildia); złote z pamięci ciała, białe z konfiguracji wioski.

## Pamięć: wspomnienia, epizody i sieć znaczeń

- **Wspomnienie:** zapis jednego zdarzenia z wyników tury albo dziennika ciała (typ, waga, licznik powtórzeń, tura, tick, pozycja, krótki kontekst).
- **Waga:** liczba porządkująca wspomnienia do konsolidacji (śmierć 10, handel 4, utknięcie 4, walka 3, odkrycie 2, błąd 2, przejęcie 1; pierwsze zdarzenie typu +3, nowy kod błędu +3, powtórzenie +1).
- **Pewność:** jak bardzo wynik wspomnienia jest potwierdzony (wysoka: wynik w odpowiedzi moda; średnia: komunikat może nie mówić prawdziwej przyczyny).
- **Wynik:** co czynność zmieniła w świecie albo ekwipunku.
- **Encje:** uczestnicy czynności z typem: NPC, przedmiot, mob, narzędzie.
- **Lokacja:** nazwane miejsce czynności ze współrzędnymi i relacjami do znanych miejsc („kuźnia, 36 m SE”).
- **Rzut 2,5D z peaku:** mała izometria otoczenia w chwili najwyższej wagi epizodu, w konwencji figur (widok od SW, litery A do D).
- **Czynność poprzednia i następna:** sąsiednie kroki łańcuchów tego samego ciała w czasie, z tickami.
- **Epizod:** wspomnienie z encjami, lokacją, rzutem 2,5D z peaku, czynnością poprzednią i następną oraz wynikiem, wagą i pewnością (projekt).
- **Sieć znaczeń:** graf, węzły: encje, miejsca, czynności; krawędzie: `w_lokacji`, `po_czynnosci`, `z_udzialem`, `daje_wynik`, `kosztuje` (projekt).
- **Konsolidacja:** zamiana wspomnień w lekcje przy zatrzymanym świecie przez subagenta tylko do odczytu, ze strażnikiem zapisu.
- **Wyzwalacze D i E:** D = co najmniej 8 nieopisanych wspomnień, E = suma wag co najmniej 20 (min. 3, maks. 15 tur odstępu).

## Drzewa decyzyjne

- **Punkt decyzyjny:** klatka decyzyjna jednej tury: tura, tick, ciało, wyzwalacz, sytuacja z klatki, plan.
- **Wyzwalacz:** powód wywołania modelu (koniec łańcucha, błąd, odkrycie, zagrożenie, watchdog); jego brak oznacza rundę bez wywołania.
- **Odruch:** decyzja bez rozumowania (0 tokenów rozumowania i mniej niż 25 słów przed akcją).
- **Rozważanie:** decyzja z tokenami rozumowania albo z dłuższym tekstem przed akcją.
- **Plan:** linia `PLAN:` modelu, przenoszona między turami przez łańcuch i dziennik.
- **Gałąź wybrana / alternatywa:** przyjęty łańcuch (gruba gałąź, kolor kategorii) i niewybrane pozycje menu z tej samej tury (cienkie, szare).
- **Peak (★) i rozwidlenie (⑂):** kulminacja przebiegu i miejsce, w którym inna decyzja albo inny wyzwalacz dałby inny przebieg.
