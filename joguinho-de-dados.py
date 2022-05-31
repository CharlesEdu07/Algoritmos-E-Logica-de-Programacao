import random

def draw_dice(num):
    if num == 1:
        print("""
-------
|     |
|  O  |
|     |
-------""")

    elif num == 2:
        print("""
-------
|   o |
|     |
| o   |
-------
        """)

    elif num == 3:
        print("""
-------
|   o |
|  o  |
| o   |
-------
        """)

    elif num == 4:
        print("""
-------
| o o |
|     |
| o o |
-------
        """)

    elif num == 5:
        print("""
-------
| o o |
|  o  |
| o o |
-------
        """)

    else:
       print("""
-------
| o o |
| o o |
| o o |
-------
        """) 

partidas = 0

somajog = 0

somacom = 0

print("""O jogo consiste em três lançamentos de dados.
A soma dos três dados lançados por cada
um dos jogadores definirá o vencedor!""")

op = int(input("\nDigite 1 para iniciar o jogo \nDigite 2 para sair\n\nOpção: "))

if op == 1:
    print("\nIniciando o jogo")

    print("\nRolando os dados!")

    jogd1 = random.randint(1,6)
    jogd2 = random.randint(1,6)
        
    comd1 = random.randint(1,6)
    comd2 = random.randint(1,6)

    print("\nDados do jogador: ")
    draw_dice(jogd1)
    draw_dice(jogd2)

    print("\nDados do computador: ")
    draw_dice(comd1)
    draw_dice(comd2)

    print("\nSomando os valores...")

    somajog = jogd1 + jogd2
    somacom = comd1 + comd2


if somajog > somacom:
    print("\nJOGADOR VENCEU! \nPLACAR: " , somajog , "VS" , somacom)

elif somacom > somajog:
    print("\nCOMPUTADOR VENCEU! \nPLACAR: " , somacom , "VS" , somajog)

else:
    print("\nEMPATE! \nPLACAR: " , somacom , "VS" , somajog)

print("\nEncerrando...")


