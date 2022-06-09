while(1==1):
    numero1 = float(input('Informe o primeiro número: '))
    numero2 = float(input('Informe o segundo número: '))

    print("[1] - SOMA")
    print("[2] - SUBTRAÇÃO")
    print("[3] - MULTIPLICAÇÃO")
    print("[4] - DIVISÃO")
    operacao = int(input('\nEscolha a operação que deseja realizar: '))

    if(operacao == 1):
        result = numero1+numero2
    elif(operacao == 2):
        result = numero1-numero2
    elif(operacao == 3):
        result = numero1*numero2
    else:
        result = numero1/numero2

    if(result % 2 == 0):
        print("O número {} é um número par.".format(result))
    else:
        print("O número {} é um número ímpar.".format(result))

    if(result > 0):
        print("O número {} é um número positivo.".format(result))
    elif(result == 0):
        print("O número {} é um número nulo.".format(result))
    else:
        print("O número {} é um número negativo.".format(result))

    if(result // 1 == result):
        print("O número {} é um número inteiro.".format(result))
    else:
        print("O número {} é um número decimal.".format(result))