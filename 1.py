autos = [
    {"marca": "Toyota", "modelo": "Corolla", "anio": 2020},
    {"marca": "Honda", "modelo": "Civic", "anio": 2018},
    {"marca": "Ford", "modelo": "Focus", "anio": 2019},
    {"marca": "Nissan", "modelo": "Sentra", "anio": 2021}
]

clave = "modelo"

ordenados = sorted(autos, key=lambda x: x[clave])

for n in ordenados:
    print(n)