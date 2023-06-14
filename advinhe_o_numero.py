from random import randint

chances = 10
vezes = 1

print("\nTente advinhar o número que o computador irá sortear")

com = randint(1, 100)
    
print("\nO computador já sorteou um número")

while chances > 0:
    op = int(input("\nDigite um valor entre 1 e 100: "))

    if op > 0 and op <= 100:
        if op == com and vezes == 1:
            print("\nVOCÊ TEVE MUITA SORTE")

            print("\nVocê fez", vezes, "tentativas até acertar")

            op2 = input("\nDeseja jogar novamente? (s ou n): ")

            if op2 == "s":
                com = randint(1, 100)
               
                chances = 10
                vezes = 1

            else:
                chances = 0

        elif op == com and vezes == 2:
            print("\nVOCÊ JOGA BEM, MAS AINDA CONTOU SORTE")

            print("\nVocê fez", vezes, "tentativas até acertar")

            chances = 0

            op2 = input("\nDeseja jogar novamente? (s ou n): ")

            if op2 == "s":
                com = randint(1, 100)
                
                chances = 10
                vezes = 1

            else:
                chances = 0

        elif op == com and vezes == 3:
            print("\nVOCÊ É UM EXCELENTE ESTRATEGISTA")

            print("\nVocê fez", vezes, "tentativas até acertar")

            op2 = input("\nDeseja jogar novamente? (s ou n): ")

            if op2 == "s":
                com = randint(1, 100)
                
                chances = 10
                vezes = 1

            else:
                chances = 0

        elif op == com and vezes > 3:
            print("\nDemorou, mas acertou")

            print("\nVocê fez", vezes, "tentativas até acertar")

            op2 = input("\nDeseja jogar novamente? (s ou n): ")

            if op2 == "s":
                com = randint(1, 100)
                
                chances = 10
                vezes = 1

            else:
                chances = 0

        elif op != com and vezes == 10:
            print("\nANALISE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE")

            op2 = input("\nDeseja jogar novamente? (s ou n): ")

            if op2 == "s":
                com = randint(1, 100)
                
                chances = 10
                vezes = 1

            else:
                chances = 0

        elif op != com:
            print("\nErrou otário")

            print("\nDica: ")

            if op < com:
                print("Digite um número maior")

            else:
                print("Digite um número menor")
                
            vezes += 1
            chances -= 1
    else:
        print("\nVocê digitou um valor inválido. DESCLASSIFICADO")

        op2 = input("\nDeseja jogar novamente? (s ou n): ")

        if op2 == "s":
            com = randint(1, 100)
                
            chances = 10
            vezes = 1

        else:
            chances = 0

print("\nFim do programa")
