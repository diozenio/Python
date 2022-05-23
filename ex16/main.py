import math

a = float(input("Digite o valor de A:\n"))
if a != 0:
    b = float(input("Digite o valor de B:\n"))
    c = float(input("Digite o valor de C:\n"))

delta = b*b - (4*a*c)

if delta < 0:
    print('A equação não possui raizes reais')
elif delta == 0:
    raiz = -b / (2*a)
    print('Delta=0 , raiz = ', raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print('Raizes: ', raiz1, ' e ', raiz2)
