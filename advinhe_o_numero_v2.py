from random import randint

cpu_choice = randint(1, 100)

player_choice = 0

vezes = 1

limite_menor = 1
limite_maior = 100

desclassificado = False

print("Advinhe o numero!")

op = input("\nDeseja iniciar o jogo: (s ou n): ")

while op == "s" or desclassificado == False:
    print(cpu_choice)

    print("Vez de número: ", vezes)
    player_choice = int(input("\nDigite o número: "))

    if player_choice > limite_maior or player_choice < limite_menor:
        print("\nDesclassificado por burlar os limites: ", limite_menor, limite_maior)

        op2 = input("\nDeseja jogar novamente? (s ou n): ")
    
        if op2 == "s":
            vezes = 1
            limite_menor = 1
            limite_maior = 100
            cpu_choice = randint(1, 100)

        else:
            desclassificado = True
            
    elif player_choice == cpu_choice:
        if vezes <= 1:
            print("\nVOCÊ TEVE MUITA SORTE")
            print("NUMERO DE PALPITES: ", vezes)

        elif vezes <= 4:
            print("\nVOCÊ JOGA BEM, MAS AINDA CONTOU SORTE")
            print("NUMERO DE PALPITES: ", vezes)

        elif vezes <= 7:
            print("\nVOCÊ É UM EXCELENTE ESTRATEGISTA")
            print("NUMERO DE PALPITES: ", vezes)

        elif vezes <= 10:
            print("\nACERTOU, MAS PODE MELHORAR")
            print("NUMERO DE PALPITES: ", vezes)

        op2 = input("\nDeseja jogar novamente? (s ou n): ")

        if op2 == "s":
            vezes = 1
            limite_menor = 1
            limite_maior = 100
            cpu_choice = randint(1, 100)

        else:
            op = "n"

    else:
        print("\nEROOOUU")

        if player_choice > cpu_choice and vezes < 10:
            print("\nDIGITE UM NÚMERO MENOR")

            limite_maior = player_choice - 1

        elif cpu_choice > player_choice and vezes < 10:
            print("\nDIGITE UM NÚMERO MAIOR")

            limite_menor = player_choice + 1
        
        vezes += 1

    if vezes > 10:
        print("\nANALISE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE")

        op2 = input("\nDeseja jogar novamente? (s ou n): ")

        if op2 == "s":
            vezes = 1
            limite_menor = 1
            limite_maior = 100
            cpu_choice = randint(1, 100)

        else:
            op = "n"
