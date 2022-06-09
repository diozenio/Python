while True:
    valorSaque = int(input('Informe o valor: '))
    
    if(valorSaque < 10 or valorSaque > 600):
        print("Por favor, digite um saque válido.")
    else:
        valorSaqueStr = str(valorSaque)
        listvalorSaque = list(valorSaqueStr)
        tamanhoVetor = len(listvalorSaque)
        
        notasDeCem = 0
        notasDeCinquenta = 0
        notasDeDez = 0
        notasDeCinco = 0
        notasDeUm = 0
      
        if(tamanhoVetor == 3):
          
          while(notasDeCem < int(listvalorSaque[0])):
            notasDeCem+= 1
          
          if(int(listvalorSaque[1]) == 5):
            notasDeCinquenta += 1
          elif(int(listvalorSaque[1]) < 5):
            notasDeDez = int(listvalorSaque[1])
          else:
            notasDeCinquenta += 1
            notasDeDez = int(listvalorSaque[1]) - 5
          

          if(int(listvalorSaque[2]) == 5):
            notasDeCinco += 1
          elif(int(listvalorSaque[2]) < 5):
            notasDeUm = int(listvalorSaque[2])
          else:
            notasDeCinco += 1
            notasDeUm = int(listvalorSaque[2]) - 5

        elif(tamanhoVetor == 2):
          
          if(int(listvalorSaque[0]) == 5):
            notasDeCinquenta += 1
          elif(int(listvalorSaque[0]) < 5):
            notasDeDez = int(listvalorSaque[0])
          else:
            notasDeCinquenta += 1
            notasDeDez = int(listvalorSaque[1]) - 5
          

          if(int(listvalorSaque[1]) == 5):
            notasDeCinco += 1
          elif(int(listvalorSaque[1]) < 5):
            notasDeUm = int(listvalorSaque[1])
          else:
            notasDeCinco += 1
            notasDeUm = int(listvalorSaque[1]) - 5

        print(f"\nNotas de cem: {notasDeCem}") 
        print(f"Notas de cinquenta: {notasDeCinquenta}")
        print(f"Notas de dez: {notasDeDez}")
        print(f"Notas de cinco: {notasDeCinco}")
        print(f"Notas de um: {notasDeUm}")