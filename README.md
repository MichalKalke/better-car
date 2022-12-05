# better-car
## Plan inżynierki - małe zadanka na 1 posiedzenie

Zadania zrobione:

- [x] Zamówienie ładowarki samochodowej i LED'ów
- [x] Umówienie się na hamownie
- [x] Złożenie projektu - bez ledów
- [x] Skalibrowanie ekranu - nie potrzeba
- [x] Przeczytanie rozdziałów z notatkami
- [x] Umówienie sie z Maxem
- [x] Przetestowanie czy raspberry łączy się ze złączem OBD 
- [x] Zaimportowanie biblioteki pyOBD w celu sprawdzenia czy działa
- [x] Przetestowanie czy dane są zczytywane z silnika
- [x] Stworzenie prostego frontu w celu wizualizacji danych
- [x] Dodanie zamówionych elementów
- [x] Ładowanie danych z pliku na temat idealnej zmiany biegów 
- [x] Znalezienie wzoru do ECO jazdy - z wykresu z hamowni
- [x] ~~Stworzenie 2 plików wykonywalnych w zależności od wybranego modu~~ zrobione w jednym
- [ ] ~~Zastanowić się nad stworzeniem własnej biblioteki pyOBD~~

Zadania do zrobienia
- [ ] Obsługa logiki LED'ów
- [x] Obsługa LED'ów bez sudo -gpio 10 (MOSI) SPI
- [x] Obsługa LED'ów w wątku
- [x] Poprawa gui by się ładnie renderowało
- [x] ~~Zależność między obciążeniem silnika, a zużyciem paliwa~~ to jest granica bezpieczna silnika
- [x] Pogadać z Maxem
- [x] Tryb sportowy - pole pod całką mocy + przełożenia
- [x] Tryb eco do bezpiecznego pułapu + dla jazdy 40% throttle

Dane
- Bezpieczne ramy silnika: 1800rpm
- Gear ratio: 3.417, 1.958, 1.276, 0.943, 0.757, 0.634
- Final drive: 3.941

