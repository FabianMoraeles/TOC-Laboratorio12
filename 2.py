nums = list(map(int, input("Ingresa los números separados por espacio: ").split()))

n = int(input("Ingresa la potencia: "))

res = list(map(lambda x: x**n, nums))

print(res)
