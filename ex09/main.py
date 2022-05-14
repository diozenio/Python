num1 = float(input("Digite o primeiro preço: \n"))
num2 = float(input("Digite o segundo preço: \n"))
num3 = float(input("Digite o terceiro preço: \n"))

numeros = [num1, num2, num3]
numeros.sort()
print(f"O melhor produto é o que custa R${numeros[0]}0 reais")
