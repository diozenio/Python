x = 0

for a in range (3):
  nota = float(input(f"Digite a {a+1} nota: "))
  x += nota

mediaNotas = (x/3)

if (mediaNotas == 10):
  print("\nAprovado com distinção!!")
elif(mediaNotas >= 7):
  print('\nAprovado!')
else:
  print("\nReprovado")