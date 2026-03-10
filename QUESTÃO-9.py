renda_mensal = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
parcelas = int(input("Digite o numero de parcelas: "))

parcelas = emprestimo / parcelas

if emprestimo <= renda_mensal* 10 and parcelas <= renda_mensal * 0.30:
    print("Pode ser feito o emprstimo")
else:
    print("O emprestimo não pode ser feito")