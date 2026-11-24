# 1. Pytanie badawcze i metoda

> Jakie pytanie stawia esej i z jakich zapisów historii zmian powstał.

[indeks](../esej-indeks.md) · [2. Środowisko: co zbudowano →](02-srodowisko.md)

---

**Pytanie:** które techniki inżynierskie wokół modelu (wiedza, interfejs akcji, percepcja i metapoznanie środowiska) mają wpływ na skuteczność i koszt agenta LLM działającego w złożonym, zmiennym świecie, i po której stronie (model czy środowisko) leży przyczyna jego błędów?

**Metoda.** Esej nie opisuje eksperymentu kontrolowanego, tylko rekonstrukcję z historii zmian. Źródła:

- karty zadań i przebiegów agentów programujących (każde zadanie ma cel, kryteria odbioru z dowodami i raport w stałym formacie),
- raporty audytów przebiegów (tabele tur, klasyfikacja wywołań, koszt z transkryptów),
- łatki (`*.patch`) i sekcje „Wersje” w README moda, bo kod nie był wersjonowany w git, tylko w kopiach roboczych z łatkami względem poprzedniej wersji,
- zapisy przebiegów obserwacyjnych (dzienniki tur, logi ciał, klatki percepcji),
- raport przetworzenia wiedzy (objętość, sprzeczności, luki z dowodami).

Każda liczba w tekście ma źródło (plik, zadanie albo przebieg) w prywatnym aneksie autora, który nie wchodzi do wersji publicznej; liczby niepewne są tam osobno oznaczone. Liczby do figur i tabel są w [dodatkach](../dodatki/dane/).

**Zasada uczciwości:** część wyników to symulacje na kopiach logów albo testy na mocku. Zaznaczam to przy każdej liczbie, która nie pochodzi z przebiegu na żywym serwerze.

---

[indeks](../esej-indeks.md) · [2. Środowisko: co zbudowano →](02-srodowisko.md)
