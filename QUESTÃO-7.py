produto = input("Nome do produto: ")
quantidade = int(input("Quantidade do produto: "))
preço = int(input("Preço por unidade: "))

total = quantidade * preço

print(f"Total: {total}")

if quantidade <= 5:
    print("desconto de 2%")
    desconto = total - total * 2/100
    print(f"total a pagar: {desconto}")
if quantidade > 5 and quantidade <= 10:
    print("desconto de 3%")
    desconto = total - total - 3/100
    print(f"total a pagar: {desconto}")
if quantidade > 10:
    print("desconto de 5%")
    desconto = total - total * 5/100
    print(f"total a pagar: {desconto}")


