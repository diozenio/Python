print("APERTE [1] PARA 'SIM' \nAPERTE [-1] PARA 'NÃO' ")

list = []

questao1 = float(input("\nTelefonou para a vítima? "))
list.append(questao1)
questao2 = float(input("Esteve no local do crime? "))
list.append(questao2)
questao3 = float(input("Mora perto da vítima? "))
list.append(questao3)
questao4 = float(input("Devia para a vítima? "))
list.append(questao4)
questao5 = float(input("Já trabalhou com a vítima? "))
list.append (questao5)

positivo, negativo = 0, 0
for num in list: 
    
    if(num >= 0): 
        positivo += 1
    else: 
        negativo += 1
          
if(positivo == 2):
  print("\nSuspeita")
elif(positivo >= 5):
  print("\nAssassino")  
elif(positivo < 2):
  print("\nInocente")
else:
  print("\nCúmplice")