cor_cd = input("Digite a cor do CD: ")

match cor_cd:
    case "verde":
        print("valor R$10.00")
    case "azul":
        print("valor R$20.00")
    case "amarelo":
        print("valor R$30.00")
    case "vermelho":
        print("valor R$40.00")
    case _:
        print("Cor invalida")
       
       
    
    
    