valores_1 = input().split(' ')
valor1_x = float(valores_1[0])
valor1_y = float(valores_1[1])

valores_2 = input().split(' ')
valor2_x = float(valores_2[0])
valor2_y = float(valores_2[1])

distancia_x = (valor2_x - valor1_x) ** 2
distancia_y = (valor2_y - valor1_y) ** 2
distancia = (distancia_x + distancia_y) ** 0.5

print(f"{distancia:.4f}")