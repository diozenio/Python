num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
num3 = float(input("Digite o terceiro número: \n"))

numeros = [num1, num2, num3]
numeros.sort()
print(f"O maior número é {numeros[len(numeros)-1]}")
print(f"O menor número é {numeros[0]}")