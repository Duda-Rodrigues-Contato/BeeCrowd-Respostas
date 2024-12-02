valores = input().split(' ')
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maior1 = (a + b + abs(a - b)) / 2

maior2 = (maior1 + c + abs(maior1 - c)) / 2

print(f"{int(maior2)} eh o maior")