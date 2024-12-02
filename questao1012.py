valores = input().split(' ')
valor_A = float(valores[0])
valor_B = float(valores[1])
valor_C = float(valores[2])

pi = 3.14159

triangulo_retangulo = (valor_A * valor_C) / 2
circunferencia = pi * (valor_C ** 2)
trapezio = ((valor_A + valor_B) * valor_C) / 2
quadrado = valor_B ** 2
retangulo = valor_A * valor_B

print(f"TRIANGULO: {triangulo_retangulo:.3f}")
print(f"CIRCULO: {circunferencia:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")