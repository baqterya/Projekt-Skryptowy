Jakub Jędros 309677

Obecna postać gry to krótkie demo zawierające tworzenie postaci oraz jedną scenę dialogową z wyborami.

Zaimplementowałem w niej także system ekwipunku, który opiera się na klasach oraz konstrukcji "screen" wykorzystywanej w Ren'py.
Plik inventory.rpy zawiera definicję klasy ekwipunku i dziedziczące z niej klasy rodzajów przedmiotów.
Plik character.rpy zawiera definicję klasy postaci gracza i jej metody pozwalają na ekwipowanie i zdejmowanie przedmiotów.
inventory_screen.rpy zawiera wizualną część ekwipunku czyli to co i w jaki sposób wyświetla się po kliknięciu w przycisk "ekwipunek"
w trakcie gry.
items.rpy oraz images.rpy zawierają kolejno definicje przedmiotów wykorzystywanych w demie oraz przypisanie im odpowiednich obrazków.
Domyślnie folderem z którego programy napisane w Ren'py pobierają tekstury jest folder images.

Tym samym wypełniłem początkowe założenia.
