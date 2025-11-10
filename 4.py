print("Ingrese los elementos separados por espacio. Ej: [agua pan pizza]")
inicio = input("Elementos de la lista: ").split()
borrar = input("Elementos a borrar: ").split()

res = list(filter(lambda x: x not in borrar, inicio))

print("Resultado:", res)
