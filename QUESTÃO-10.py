litros = int(input("Quantidade de litros: "))
combustivel = input("Tipo de combustivel: ")

valor1 = litros * 6.59 
valor2 = litros * 3.79

if litros <= 25 and combustivel == "A":
    print("desconto de 2%")
    desconto = valor2 * 2/100
    valor_desconto = valor2 - desconto
    print(f"Valor total com o desconto: {valor_desconto}")
if litros > 25 and combustivel == "A":
    print("desconto de 4%")
    desconto = valor2 * 4/100
    valor_desconto = valor2 - desconto
    print(f"Valor total com o desconto: {valor_desconto}")
if litros <= 25 and combustivel == "G":
    print("desconto de 3%")
    desconto = valor1 * 3/100
    valor_desconto = valor1 - desconto
    print(f"Valor total com o desconto: {valor_desconto}")
if litros > 25 and combustivel == "G":
    print("desconto de 5%")
    desconto = valor1 * 5/100
    valor_desconto = valor1 - desconto

    print(f"Valor total com o desconto: {valor_desconto}")
