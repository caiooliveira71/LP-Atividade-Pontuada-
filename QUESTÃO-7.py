produto = input("Nome do produto: ")
quantidade = int(input("Quantidade do produto: "))
preço = int(input("Preço por unidade: "))

total = quantidade * preço

print(f"Total: {total}")

if quantidade <= 5:
    print("desconto de 2%")
    desconto = total * 2/100
    valor_desconto = total - desconto
    print(f"total a pagar: {valor_desconto}")
if quantidade > 5 and quantidade <= 10:
    print("desconto de 3%")
    desconto = total * 3/100
    valor_desconto = total - desconto
    print(f"total a pagar: {valor_desconto}")
if quantidade > 10:
    print("desconto de 5%")
    desconto = total * 5/100
    valor_desconto = total - desconto
    print(f"total a pagar: {valor_desconto}")



