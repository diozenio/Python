lados = []
lados.append(float(input("Digite o primeiro lado:\n"))) 
lados.append(float(input("Digite o segundo lado:\n"))) 
lados.append(float(input("Digite o terceiro lado:\n"))) 


if lados.count(lados[0]) == 2:
    print("Triângulo Isósceles")
elif lados.count(lados[1]) == 2:
    print("Triângulo Isósceles")
elif lados.count(lados[0]) == 3:
    print("Triângulo Equilátero")
elif lados.count(lados[0]) == 1:
    if lados.count(lados[1]) == 1:
        print("Triângulo Escaleno")