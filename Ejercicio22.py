# ----------------------------
# Clase List incluida aquí
# ----------------------------
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


# ----------------------------
# Ejercicio 22 - Jedi
# ----------------------------

def order_by_name(item):
    return item["nombre"]

def order_by_species(item):
    return item["especie"]

# Lista de Jedi
jedis = [
    {"nombre": "Yoda", "maestros": [], "sables": ["verde"], "especie": "desconocida"},
    {"nombre": "Luke Skywalker", "maestros": ["Yoda", "Obi-Wan Kenobi"], "sables": ["verde"], "especie": "humano"},
    {"nombre": "Anakin Skywalker", "maestros": ["Obi-Wan Kenobi"], "sables": ["azul"], "especie": "humano"},
    {"nombre": "Obi-Wan Kenobi", "maestros": ["Qui-Gon Jinn"], "sables": ["azul"], "especie": "humano"},
    {"nombre": "Ahsoka Tano", "maestros": ["Anakin Skywalker"], "sables": ["verde", "azul"], "especie": "togruta"},
    {"nombre": "Kit Fisto", "maestros": ["Yoda"], "sables": ["verde"], "especie": "nautolano"},
    {"nombre": "Mace Windu", "maestros": ["Cyslin Myr"], "sables": ["violeta"], "especie": "humano"},
    {"nombre": "Qui-Gon Jinn", "maestros": ["Conde Dooku"], "sables": ["verde"], "especie": "humano"},
    {"nombre": "Plo Koon", "maestros": ["Tyvokka"], "sables": ["naranja"], "especie": "kel dor"},
    {"nombre": "Aayla Secura", "maestros": ["Quinlan Vos"], "sables": ["azul"], "especie": "twi'lek"},
]

list_jedis = List()
list_jedis.add_criterion("nombre", order_by_name)
list_jedis.add_criterion("especie", order_by_species)

for j in jedis:
    list_jedis.append(j)

# a) Listado ordenado por nombre y especie
print("\n(a) Listado por nombre:")
list_jedis.sort_by_criterion("nombre")
list_jedis.show()

print("\n(a) Listado por especie:")
list_jedis.sort_by_criterion("especie")
list_jedis.show()

# b) Info de Ahsoka Tano y Kit Fisto
print("\n(b) Info de Ahsoka Tano y Kit Fisto:")
for name in ["Ahsoka Tano", "Kit Fisto"]:
    pos = list_jedis.search(name, "nombre")
    if pos is not None:
        print(list_jedis[pos])

# c) Padawans de Yoda y Luke Skywalker
print("\n(c) Padawans de Yoda y Luke Skywalker:")
for j in list_jedis:
    if "Yoda" in j["maestros"] or "Luke Skywalker" in j["maestros"]:
        print(j["nombre"])

# d) Jedi humanos y twi'lek
print("\n(d) Jedi humanos y twi'lek:")
for j in list_jedis:
    if j["especie"] in ["humano", "twi'lek"]:
        print(j["nombre"], "-", j["especie"])

# e) Jedi que empiezan con A
print("\n(e) Jedi que comienzan con A:")
for j in list_jedis:
    if j["nombre"].startswith("A"):
        print(j["nombre"])

# f) Jedi con más de un color de sable
print("\n(f) Jedi con más de un color de sable:")
for j in list_jedis:
    if len(j["sables"]) > 1:
        print(j["nombre"], "-", j["sables"])

# g) Jedi que usaron amarillo o violeta
print("\n(g) Jedi que usaron sable amarillo o violeta:")
for j in list_jedis:
    if "amarillo" in j["sables"] or "violeta" in j["sables"]:
        print(j["nombre"], "-", j["sables"])

# h) Padawans de Qui-Gon Jinn y Mace Windu
print("\n(h) Padawans de Qui-Gon Jinn y Mace Windu:")
for j in list_jedis:
    if "Qui-Gon Jinn" in j["maestros"] or "Mace Windu" in j["maestros"]:
        print(j["nombre"], "- maestro:", j["maestros"])
