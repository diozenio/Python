valorHora = float(input("Digite o valor da hora: "))
horasTrabalhadas = float(
    input("Digite quantas horas você trabalhou no mês: ")
)
bruto = valorHora * horasTrabalhadas
if bruto <= 900:
    descontoIR = 0.0
elif bruto <= 1500:
    descontoIR = 5
elif bruto <= 2500:
    descontoIR = 10
else:
    descontoIR = 20

IR = bruto * (descontoIR / 100)
INSS = bruto * (10 / 100)
FGTS = bruto * (11 / 100)
total = IR + INSS
salario_liquido = bruto - total

print(
    f"\nSalário Bruto     : R${bruto:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${total:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)
