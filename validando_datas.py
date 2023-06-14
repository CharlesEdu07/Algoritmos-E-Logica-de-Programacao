dia = int(input("Digite o dia: "))
mes = int(input("\nDigite o mês: "))
ano = int(input("\nDigite o ano: "))

#31 dias - Janeiro(1), Março(3), Maio(5), Julho(7), Agosto(8), Outubro(10), Dezembro(12)
#30 dias - Abril(4), Junho(6), Setembro(9), Novembro(11)
#28 ou 29 - Fevereiro(2)

is_bissexto = False

if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
    is_bissexto = True

if dia > 0 and mes > 0 and ano > 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            print("\nData válida", dia, "/", mes, "/", ano)

            if is_bissexto: print("ANO BISSEXTO")

        else:
            print("\nData inválida, pois no mes", mes, "não existe dia correspondente ao inserido")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            print("\nData válida", dia, "/", mes, "/", ano)

            if is_bissexto: print("ANO BISSEXTO")

        else:
            print("\nData inválida, pois no mes", mes, "não existe dia correspondente ao inserido")

    elif mes == 2:
        if dia <= 28:
            print("\nData válida", dia, "/", mes, "/", ano)

            if is_bissexto: print("ANO BISSEXTO")

        elif dia == 29 and is_bissexto:
            print("\nData válida", dia, "/", mes, "/", ano, "ANO BISSEXTO")

        else:
            print("\nData inválida, pois no mes", mes, "não existe dia correspondente ao inserido")

else:
    print("\nData inválida, pois dia, mês ou ano estão iguais ou menores que 0")
