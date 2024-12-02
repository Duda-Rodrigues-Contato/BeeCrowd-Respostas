nome_vendedor = input("")
salario_fixo = float(input(""))
valor_vendas_mes = float(input(""))

salario_bonus = salario_fixo + ((15/100) * valor_vendas_mes)

print(f"TOTAL = R$ {salario_bonus:.2f}")