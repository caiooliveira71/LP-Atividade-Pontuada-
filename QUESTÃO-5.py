valorA = int(input("valor de A: "))
valorB = int(input("valor de B: "))
operadores = input("Digite um dos operadores(+,-,*,/): ")

match operadores:
    case "-":
        resultado = valorA - valorB
        print("{} - {} = {}".format(valorA, valorB, resultado))
    case "+":
        resultado2 = valorA + valorB
        print("{} + {} = {}".format(valorA, valorB, resultado2))
    case "*":
        resultado3 = valorA * valorB
        print("{} * {} = {}".format(valorA, valorB, resultado3))
    case "/":
        resultado4 = valorA / valorB
        print("{} / {} = {}".format(valorA, valorB, resultado4))
    case _:
        print("operador invalido")