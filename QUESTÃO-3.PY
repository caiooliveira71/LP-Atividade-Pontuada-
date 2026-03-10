A = int(input("digite o valor de A: "))
B = int(input("digite o valor de B: "))

if A == B:
    print("São iguais")
    resultado = A + B
else:
    print("Não são iguais")
    resultado = A * B
    
C = resultado

print(f"Valor de C: {C}")