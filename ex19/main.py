numero = int(input("Digite um número:\n"))

if numero < 1000 and numero > 0:
    texto = str(numero)
    print(texto[0], " centenas, ", texto[1],
          " dezenas, ", texto[2], " unidades.")
else:
    print("Número inválido")
