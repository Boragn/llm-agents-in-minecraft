# Protokół: tor kontrolny przed scenariuszem

[indeks](../esej-indeks.md) · [dodatki](README.md) · [rozdział 8](../czesc-2-percepcja-i-metapoznanie/08-metapoznanie.md)

Cel: sprawdzić narzędzia ciała, zanim zrobi to model za pieniądze. Osiem prób na torze zbudowanym poleceniami serwera w osobnym obszarze świata, każda z oczekiwanym wynikiem i diagnozą typu błędu. Status: zdefiniowany i sprawdzony na mocku, nie uruchomiony na żywo.

| # | próba | oczekiwany wynik | co diagnozuje porażka |
|---|---|---|---|
| 1 | drzwi drewniane w ścianie | ciało przechodzi przez drzwi | planer albo obsługa drzwi |
| 2 | drabina 4 bloki | ciało wchodzi i schodzi | ruch pionowy (drabina) |
| 3 | schody | ciało wchodzi bez skoku | krok, półpłytka |
| 4 | luka 1 i 2 pola | przeskok bez upadku | skok, zasięg |
| 5 | woda | przepłynięcie i wyjście | ruch w wodzie |
| 6 | skrzynia przy ścianie | `wyjmij` i `wloz` działają | dojście do kontenera (cel w bloku) |
| 7 | stół rzemieślniczy | craft wymagający stołu | stół w zasięgu |
| 8 | płot z furtką | przejście przez furtkę | furtka, płot 1,5 bloku |

Werdykt: PASS albo FAIL dla każdej próby; FAIL z typem bloku i sygnałem detektora (S1..S8) trafia do operatora przed startem scenariusza.
