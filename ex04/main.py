vogais = ("a", "e", "i", "o", "u")
letra = input("Digite uma letra: \n")

if vogais.__contains__(letra) and len(letra) == 1:
    print("Vogal")
elif len(letra)!= 1:
    print("Inválido")
else:
    print("Consoante")