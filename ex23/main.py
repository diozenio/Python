while(1==1):
  num = float(input('\nInforme o número: '))
  numArredondado = round(num)
  
  if(num // 1 == num):
    print("\nO número {} é inteiro".format(num))
  else:
    print("\nO número {} é decimal".format(num))
    print("\nNúmero arredondado:{}".format(numArredondado))