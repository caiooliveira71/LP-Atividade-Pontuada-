aluno = input("Digite o nome do aluno: ")
nota1 = int(input("Primeira nota: "))
nota2 = int(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Media: {media}")

if media >= 6:
    print("Parabens voçe foi aprovado")
if 4 <= media < 6:
    print("Voçe esta de recuperação")
if media < 4:
    print("Que pena voçe foi reprovado")