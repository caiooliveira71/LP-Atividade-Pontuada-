produto = input("Nome do produto: ")
quantidade = int(input("Quantidade do produto: "))
preço = int(input("Preço por unidade: "))

total = quantidade * preço

print(f"Total: {total}")

if quantidade <= 5:
    print("desconto de 2%")
    desconto = 2/100
    total_pagar = total - desconto
    print(f"total a pagar: {total_pagar}")
if quantidade > 5 and quantidade <= 10:
    print("desconto de 3%")
    desconto = 3/100
    total_pagar = total - desconto
    print(f"total a pagar: {total_pagar}")
if quantidade > 10:
    print("desconto de 5%")
    desconto = 5/100
    total_pagar = total - desconto
    print(f"total a pagar: {total_pagar}")

