# Protokół eksperymentu: czy agent sam rozumie klatkę (metapoznanie, poziom 2)

[indeks](../esej-indeks.md) · [dodatki](README.md) · [rozdział 8](../czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md)

Status: projekt, niezlecony. Kopia protokołu z rozdziału 8.2, tu jako samodzielny dokument do uruchomienia.

**Planowany eksperyment (protokół; jeszcze niezlecony, czeka na decyzję operatora).**

1. **Warunki klatki:** (A) klatka z legendą i z `opis-klatki.md` jak w WY-8 (punkt odniesienia); (B) klatka z legendą, bez dokumentacji; (C) klatka bez legendy i bez dokumentacji; (D) klatka z **zamienioną legendą** (np. `L` opisane jako woda, `@` jako skrzynia): test, czy model wierzy legendzie, czy temu, co widzi w układzie mapy i w skutkach akcji.
2. **Pytania kontrolne** na tych samych klatkach (zestaw jak 21 pytań z [rozdz. 7](../czesc-2-percepcja-i-metapoznanie/07-projekcja-3d-na-2d.md): gdzie jestem, dokąd prowadzi łańcuch, co było w poprzedniej klatce, ile bloków ma jeden znak mapy 2D, czy dojdę do skrzyni), oceniane jak tam: tak, częściowo, nie.
3. **Odkrywanie przez działanie:** w warunkach C i D krótki przebieg z akcjami odczytu i ruchu; miara to liczba tur do poprawnej interpretacji znaków i skali (np. czy po kroku na wschód model zauważa, że `@` przesunął się w prawo) oraz czy model sam zapisuje swoją legendę w notatce.
4. **Porównanie modeli:** Haiku, Sonnet i Opus na tych samych klatkach i pytaniach, z kosztem na poprawną odpowiedź.
5. **Kryterium:** poziom 2 uznaję za obecny, gdy w warunku C model odpowiada na co najmniej połowę pytań tak dobrze jak w A, a w warunku D wykrywa sprzeczność legendy z układem mapy, zamiast ją ślepo stosować.

> **Wynik eksperymentu: do uzupełnienia.** Eksperyment nie był uruchomiony; ta sekcja zostanie wypełniona po decyzji operatora i przebiegu.

## Dane do zapisania

- dla każdego warunku i modelu: klatka (plik tekstowy), pytania, odpowiedzi, ocena (tak, częściowo, nie), koszt i liczba tur,
- w warunkach C i D: kolejne pozycje ciała i komentarze modelu do czasu poprawnej interpretacji znaków i skali,
- wynik zbiorczy w CSV w `dane/`.
