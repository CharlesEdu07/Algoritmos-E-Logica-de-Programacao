import random

vet = ["Pedra", "Papel", "Tesoura"]

escolhajog = 0
escolhacom = 0

print("Joguinho pedra, papel e tesoura")

op = int(input("\nDigite 1 para começar: "))

if op == 1:
    print("\n--------------------------------")
    
    op2 = int(input("""\nDigite 1 para pedra
\nDigite 2 para papel
\nDigite 3 para tesoura
\nSua escolha: """))

    if op2 == 1:
        escolhajog = vet[0]

    elif op2 == 2:
        escolhajog = vet[1]

    else:
        escolhajog = vet[2]

    escolhacom = random.choice(vet)

    print("\nSua escolha foi: " , escolhajog)
    print("A escolha do computador foi: " , escolhacom)

    if escolhajog == "Pedra" and escolhacom == "Papel":
        print("\nO COMPUTADOR GANHOU!")

    elif escolhajog == "Pedra" and escolhacom == "Tesoura":
        print("\nVOCÊ GANHOU!")

    elif escolhajog == "Papel" and escolhacom == "Tesoura":
        print("\nO COMPUTADOR GANHOU!")

    elif escolhajog == "Papel" and escolhacom == "Pedra":
        print("\nVOCÊ GANHOU!")

    elif escolhajog == "Tesoura" and escolhacom == "Pedra":
        print("\nO COMPUTADOR GANHOU!")

    elif escolhajog == "Tesoura" and escolhacom == "Papel":
        print("\nVOCÊ GANHOU!")

    else:
        print("\nEMPATE!")

print("\n--------------------------------")
print("\nEncerrando...")
