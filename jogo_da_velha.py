from random import randint

matriz = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

p1_win = False
p2_win = False
empate = False

vez = randint(0, 1)

print(vez)

op = input("Deseja iniciar o jogo? (s ou n): ")

print("\nJogador ", vez + 1, "começa")

while op == "s":
    print()

    for i in range(3):
        print('|', end='')
    
        for j in range(3):
            print('%3s'%matriz[i][j], end='')

        print(' |')

    if vez == 0:
        print("\nVez do jogador:", vez + 1, "(X)")
        jogada = int(input("Digite a posição para fazer a jogada: "))
        
        i = (jogada - 1) // 3
        j = (jogada - 1) % 3

        if matriz[i][j] != "X" and matriz[i][j] != "O" and matriz[i][j] == "-":
            matriz[i][j] = "X"

            vez = 1

        else:
            print("\nMovimento inválido, digite novamente")

            vez = 0

    elif vez == 1:
        print("\nVez do jogador:", vez + 1, "(O)")
        jogada = int(input("Digite a posição para fazer a jogada: "))
        
        i = (jogada - 1) // 3
        j = (jogada - 1) % 3

        if matriz[i][j] != "X" and matriz[i][j] != "O" and matriz[i][j] == "-":
            matriz[i][j] = "O"

            vez = 0

        else:
            print("\nMovimento inválido, digite novamente")

            vez = 1

    #-------------------------------------------------------------------------------

    if matriz[0][0] == matriz[0][1] and matriz[0][1] == matriz[0][2] and matriz[0][2] != '-':
        if matriz[0][0] == "X":
            p1_win = True

        else:
            p2_win = True

    elif matriz[1][0] == matriz[1][1] and matriz[1][1] == matriz[1][2] and matriz[1][2] != '-':
        if matriz[1][0] == "X":
            p1_win = True

        else:
            p2_win = True

    elif matriz[2][0] == matriz[2][1] and matriz[2][1] == matriz[2][2] and matriz[2][2] != '-':
        if matriz[2][0] == "X":
            p1_win = True

        else:
            p2_win = True

    #-------------------------------------------------------------------------------

    elif matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[2][2] != '-':
        if matriz[0][0] == "X":
            p1_win = True

        else:
            p2_win = True

    elif matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[2][0] != '-':
        if matriz[0][2] == "X":
            p1_win = True

        else:
            p2_win = True

    #-------------------------------------------------------------------------------

    elif matriz[0][0] == matriz[1][0] and matriz[1][0] == matriz[2][0] and matriz[2][0] != '-':
        if matriz[0][0] == "X":
            p1_win = True

        else:
            p2_win = True

    elif matriz[0][1] == matriz[1][1] and matriz[1][1] == matriz[2][1] and matriz[2][1] != '-':
        if matriz[0][1] == "X":
            p1_win = True

        else:
            p2_win = True

    elif matriz[0][2] == matriz[1][2] and matriz[1][2] == matriz[2][2] and matriz[2][2] != '-':
        if matriz[0][2] == "X":
            p1_win = True

        else:
            p2_win = True

    elif matriz[0][0] != "-" and matriz[0][1] != "-" and matriz[0][2] != "-" and matriz[1][0] != "-" and matriz[1][1] != "-" and matriz[1][2] != "-" and matriz[2][0] != "-" and matriz[2][1] != "-" and matriz[2][2] != "-":
        empate = True

    if p1_win:
        print()

        for i in range(3):
            print('|', end='')
    
            for j in range(3):
                print('%3s'%matriz[i][j], end='')

            print(' |')
        
        print("\nJogador 1 ganhou")

        op = input("Deseja jogar novamente? (s ou n): ")

        if op == "s":
            matriz = [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]
            ]

            vez = 0
            p1_win = False
            p2_win = False

        else:
            op = "n"

    elif p2_win:
        print()

        for i in range(3):
            print('|', end='')
    
            for j in range(3):
                print('%3s'%matriz[i][j], end='')

            print(' |')
        
        print("\nJogador 2 venceu")

        op = input("Deseja jogar novamente? (s ou n): ")

        if op == "s":
            matriz = [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]
            ]

            vez = 0
            p1_win = False
            p2_win = False

        else:
            op = "n"

    elif empate:
        for i in range(3):
            print('|', end='')
    
            for j in range(3):
                print('%3s'%matriz[i][j], end='')

            print(' |')
        
        print("\nEmpate")

        op = input("Deseja jogar novamente? (s ou n): ")

        if op == "s":
            matriz = [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]
            ]

            vez = 0
            p1_win = False
            p2_win = False

        else:
            op = "n"
