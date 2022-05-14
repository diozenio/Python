altura = float(input("Qual sua altura?\n"))
peso = float(input("Qual seu peso?\n"))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"abaixo do peso {imc}")
elif imc >= 18.5 and imc < 25:
    print(f"peso saudável {imc}")
elif imc >= 25 and imc < 30:
    print(f"sobrepeso {imc}")
elif imc >= 30 and imc < 40:
    print(f"obeso {imc}")
else:
    print(f"obeso mórbido {imc}")
