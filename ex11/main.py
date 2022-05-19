salario = float(input("Digite o salário do colaborador:\n"))

if salario < 280 and salario > 0: 
    aumento = 20
elif salario >= 280 and salario < 700:
    aumento = 15
elif salario >= 700 and salario < 1500:
    aumento = 10
elif salario >= 1500:
    aumento = 5

novo_salario = salario + (salario*aumento/100)

print(f"O salário de R${salario}0 recebeu um aumento de {aumento}% e agora será R${novo_salario}0")