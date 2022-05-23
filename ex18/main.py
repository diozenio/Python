from operator import truediv


data = input("Informe uma data dd/mm/aaaa:\n")
divisao = data.split("/")

validacao = False

if int(divisao[0]) > 0 and int(divisao[1]) > 0 and int(divisao[2]) > 0 and int(divisao[0]) <= 31 and int(divisao[1]) <= 12:
    validacao = True

if validacao == True:
    print("Válida")
else:
    print("Inválida")
