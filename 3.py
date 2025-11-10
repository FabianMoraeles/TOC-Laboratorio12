n = int(input("Filas: "))
m = int(input("Columnas: "))
print("Ingrese los datos separado con espacio. Ejem: [1 2 3 4]")

matriz = []
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    matriz.append(fila)

r = list(map(lambda *f: list(f), *matriz))


print("")
print("Matriz transpuesta:")
for j in r:
    print(j)
