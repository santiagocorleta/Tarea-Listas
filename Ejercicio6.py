from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(self, key_criterion: str, function):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self) -> None:
        for element in self:
            print(element)

    def delete_value(self, value, key_value: str = None) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    def sort_by_criterion(self, criterion_key: str = None) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)
        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print("criterio de orden no encontrado")

    def search(self, search_value, search_key: str = None) -> int:
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) - 1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1
            middle = (start + end) // 2
        return None

# Ejercicio 6 

def order_by_name(item):
    return item["name"]

def order_by_year(item):
    return item["first_appearance"]

# Lista de superhéroes
superheroes = [
    {"name": "Linterna Verde", "first_appearance": 1940, "casa": "DC", "bio": "Héroe con anillo de poder"},
    {"name": "Wolverine", "first_appearance": 1974, "casa": "Marvel", "bio": "Mutante con garras y traje amarillo"},
    {"name": "Dr Strange", "first_appearance": 1963, "casa": "DC", "bio": "Hechicero supremo"},
    {"name": "Capitana Marvel", "first_appearance": 1968, "casa": "Marvel", "bio": "Carol Danvers con armadura Kree"},
    {"name": "Mujer Maravilla", "first_appearance": 1941, "casa": "DC", "bio": "Princesa amazona con traje mítico"},
    {"name": "Flash", "first_appearance": 1940, "casa": "DC", "bio": "Hombre más rápido del mundo"},
    {"name": "Star-Lord", "first_appearance": 1976, "casa": "Marvel", "bio": "Héroe galáctico con armadura especial"},
    {"name": "Batman", "first_appearance": 1939, "casa": "DC", "bio": "Murciélago con traje y gadgets"},
    {"name": "Spider-Man", "first_appearance": 1962, "casa": "Marvel", "bio": "Hombre araña con traje rojo y azul"},
    {"name": "Superman", "first_appearance": 1938, "casa": "DC", "bio": "Kryptoniano con traje azul y capa roja"},
]

list_superheroes = List()
list_superheroes.add_criterion("name", order_by_name)
list_superheroes.add_criterion("year", order_by_year)

for hero in superheroes:
    list_superheroes.append(hero)

# a) Eliminar Linterna Verde
print("\n(a) Eliminar Linterna Verde:")
print(list_superheroes.delete_value("Linterna Verde", "name"))

# b) Año de Wolverine
print("\n(b) Año de aparición de Wolverine:")
pos = list_superheroes.search("Wolverine", "name")
if pos is not None:
    print(list_superheroes[pos]["first_appearance"])

# c) Cambiar casa de Dr Stange a Marvel
print("\n(c) Cambiar casa de Dr Strange:")
pos = list_superheroes.search("Dr Strange", "name")
if pos is not None:
    list_superheroes[pos]["casa"] = "Marvel"
    print(list_superheroes[pos])

# d) Biografía con “traje” o “armadura”
print("\n(d) Superhéroes con 'traje' o 'armadura':")
for hero in list_superheroes:
    if "traje" in hero["bio"].lower() or "armadura" in hero["bio"].lower():
        print(hero["name"])

# e) Aparición antes de 1963
print("\n(e) Superhéroes antes de 1963:")
for hero in list_superheroes:
    if hero["first_appearance"] < 1963:
        print(hero["name"], "-", hero["casa"])

# f) Casa de Capitana Marvel y Mujer Maravilla
print("\n(f) Casa de Capitana Marvel y Mujer Maravilla:")
for name in ["Capitana Marvel", "Mujer Maravilla"]:
    pos = list_superheroes.search(name, "name")
    if pos is not None:
        print(name, "->", list_superheroes[pos]["casa"])

# g) Info de Flash y Star-Lord
print("\n(g) Info de Flash y Star-Lord:")
for name in ["Flash", "Star-Lord"]:
    pos = list_superheroes.search(name, "name")
    if pos is not None:
        print(list_superheroes[pos])

# h) Nombres que empiezan con B, M o S
print("\n(h) Superhéroes que empiezan con B, M o S:")
for hero in list_superheroes:
    if hero["name"].startswith(("B", "M", "S")):
        print(hero["name"])

# i) Conteo por casa
print("\n(i) Cantidad por casa:")
conteo = {"Marvel": 0, "DC": 0}
for hero in list_superheroes:
    conteo[hero["casa"]] += 1
print(conteo)
