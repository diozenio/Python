print("Digite seu turno:")
print("M-matutino\nV-Vespertino\nN- Noturno.")
turno = input()

if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Valor Inválido!")
