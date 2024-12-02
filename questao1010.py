valores_1 = input().split(' ')
codigo_produto_1 = int(valores_1[0])
qtd_de_unidades_1 = int(valores_1[1]) 
preco_por_unidade_1 = float(valores_1[2])

valores_2 = input().split(' ')
codigo_produto_2 = int(valores_2[0]) 
qtd_de_unidades_2 = int(valores_2[1]) 
preco_por_unidade_2 = float(valores_2[2])

valor_total = ((qtd_de_unidades_1 * preco_por_unidade_1) + (qtd_de_unidades_2 * preco_por_unidade_2))

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")