# Wyniki testu percepcji

[artykuł](../../README.pl.md) · [article (EN)](../../README.md) · [dodatki](../README.md)

Wejscia: rzuty klatka, p1, p2 i p4 dwoch scen w [surowych klatkach](../klatki-surowe/README.md). Ocena: subagent Sonnet, wsady po 24 pozycje w losowej kolejnosci, bez nazwy wariantu i modelu. Trafnosc = suma ocen (1 / 0,5 / 0) z 6 pytan (2 sceny x 3), srednia z 3 powtorzen. Tokeny = znaki pliku / 3 (wc -c), srednia z 2 scen.

## Razem (2 sceny, 6 pytan)

| wariant | model | trafnosc (0-6) | rozrzut min-max | tokeny | trafnosc na 1000 tok. |
|---|---|---|---|---|---|
| klatka | haiku | 4.33 | 4.0-4.5 | 2998 | 1.45 |
| klatka | sonnet | 4.50 | 4.0-5.0 | 2998 | 1.50 |
| p1 | haiku | 2.83 | 2.0-3.5 | 2589 | 1.09 |
| p1 | sonnet | 3.83 | 3.5-4.0 | 2589 | 1.48 |
| p2 | haiku | 5.33 | 5.0-5.5 | 495 | 10.77 |
| p2 | sonnet | 5.33 | 5.0-5.5 | 495 | 10.77 |
| p4 | haiku | 5.50 | 5.0-6.0 | 1571 | 3.50 |
| p4 | sonnet | 4.67 | 4.0-5.5 | 1571 | 2.97 |

## Scena domek-wnetrze (3 pytania, 0-3)

| wariant | model | trafnosc (0-3) | rozrzut min-max | tokeny | trafnosc na 1000 tok. |
|---|---|---|---|---|---|
| klatka | haiku | 2.00 | 2.0-2.0 | 3120 | 0.64 |
| klatka | sonnet | 2.50 | 2.0-3.0 | 3120 | 0.80 |
| p1 | haiku | 1.83 | 0.5-2.5 | 2590 | 0.71 |
| p1 | sonnet | 1.83 | 1.5-2.0 | 2590 | 0.71 |
| p2 | haiku | 2.83 | 2.5-3.0 | 525 | 5.40 |
| p2 | sonnet | 2.50 | 2.5-2.5 | 525 | 4.76 |
| p4 | haiku | 2.67 | 2.5-3.0 | 1565 | 1.70 |
| p4 | sonnet | 2.50 | 2.5-2.5 | 1565 | 1.60 |

## Scena mur-horda (3 pytania, 0-3)

| wariant | model | trafnosc (0-3) | rozrzut min-max | tokeny | trafnosc na 1000 tok. |
|---|---|---|---|---|---|
| klatka | haiku | 2.33 | 2.0-2.5 | 2876 | 0.81 |
| klatka | sonnet | 2.00 | 2.0-2.0 | 2876 | 0.70 |
| p1 | haiku | 1.00 | 0.5-1.5 | 2587 | 0.39 |
| p1 | sonnet | 2.00 | 2.0-2.0 | 2587 | 0.77 |
| p2 | haiku | 2.50 | 2.0-3.0 | 465 | 5.38 |
| p2 | sonnet | 2.83 | 2.5-3.0 | 465 | 6.09 |
| p4 | haiku | 2.83 | 2.5-3.0 | 1577 | 1.80 |
| p4 | sonnet | 2.17 | 1.5-3.0 | 1577 | 1.37 |

## Wniosek wobec hipotezy

Hipoteza: p4 i p2 daja wyzsza trafnosc niz obecna klatka przy mniejszej liczbie tokenow; obalona, jesli klatka ma trafnosc nie nizsza niz p4 dla obu modeli.
- Haiku: klatka 4,33 vs p4 5,50 vs p2 5,33. Sonnet: klatka 4,50 vs p4 4,67 vs p2 5,33.
- Klatka nie jest nie nizsza niz p4 dla zadnego modelu, wiec warunek obalenia nie zachodzi. Tokeny: p4 to ok. 1571 (klatka 2998), p2 to ok. 495.
- **Hipoteza potwierdzona co do kierunku, z dwoma zastrzezeniami:** (1) dla Sonneta p4 vs klatka to roznica 0,17 przy nakladajacych sie rozrzutach (4,0-5,5 vs 4,0-5,0), czyli dla tej pary wynik nierozstrzygniety; wyrazna przewaga p4 jest tylko dla Haiku. (2) p2 (afordancje z tabela radaru) wygrywa najczytelniej: wyzsza trafnosc u obu modeli (5,33 vs 4,33 i 4,50) przy ok. 6 razy mniejszej liczbie tokenow (trafnosc na 1000 tok. 10,8 vs 1,5).
- p1 (przejezdnosc 2,5D) jest najslabszy: nizszy niz klatka u obu modeli, przy podobnym koszcie tokenow. Nie jest czescia hipotezy, ale warto to odnotowac.

## Zastrzezenia

- 2 sceny i 6 pytan: sygnal, nie dowod statystyczny. Jeden krok oceny to 0,5, wiec rozrzuty 0,5-1,0 to szum.
- Scena mur-horda jest syntetyczna; p2 zawiera gotowe afordancje i tabele radaru, wiec model w czesci kopiuje odpowiedz z pliku, a nie wnioskuje z rzutu. To mierzy uzytecznosc formatu, nie wnioskowanie z mapy.
- Powtorzenie 1 Haiku przepisal agent prowadzacy test (czesc skrocona bez zmiany tresci); pozostale odpowiedzi model zapisal sam.
- Oceniajacy to jedna instancja Sonneta (te same wsady, bez powtorzen oceny); modele testowane i oceniajacy to ta sama rodzina, mozliwe ukryte przychylnosc lub blad systematyczny. Prawda dla q3 domku (dziura w podlodze) bywa trudna dla kazdego wariantu.
- Tokeny to przyblizenie znaki/3, nie licznik tokenizera.

Figura: [fig-trafnosc-tokeny.svg](fig-trafnosc-tokeny.svg) (kropka: srednia, kreska: min-max).
