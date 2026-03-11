morango = int(input("Quantidade de morangos em kg: "))
maças = int(input("Quantidade de maças em kg: "))

total = morango * maças
valor_morango = 2.50 * morango
valor_maças = 1.80 * maças
valor_total = valor_morango + valor_maças
desconto = valor_total - valor_total

print(f"Valor a ser pago: {valor_total}")

if valor_total > 15 or total >= 10:
    print("Desconto de 10%")
    print(f"quantidade de morangos: {morango}")
    print(f"quantidade de maças: {maças}")
    print(f"Voçe ira pagar com desconto: {desconto}")
else:
    print(f"quantidade de morangos: {morango}")
    print(f"quantidade de maças: {maças}")
    print(f"Voçe ira pagar: {valor_total}")
