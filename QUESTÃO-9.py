renda_mensal = float(input("digite sua renda mensal: "))
emprestimo = float(input("digiteo valor do emprestimo: "))
num_parcelas = int(input("digite a quantidade de parcelas: "))

parcelas = emprestimo / num_parcelas

if emprestimo <= renda_mensal * 10 and parcelas <= renda_mensal * 0.30:
    print("pode ser feito um emprestimo")
else:
    print("não pode ser feito um emprestimo")