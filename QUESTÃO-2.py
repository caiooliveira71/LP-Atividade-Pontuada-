nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estado_civil = input("Digite seu estado civil: ")

if sexo == "F" and estado_civil == "casada":
    print("Solicitar tempo de casado")
    
print("-Dados do Usuario-")
print(f"nome: {nome}")
print(f"sexo: {sexo}")
print(f"Estado civil: {estado_civil}")