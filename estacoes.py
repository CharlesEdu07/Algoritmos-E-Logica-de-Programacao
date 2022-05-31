dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

hemisferio = input("""\nDigite o hemisfério: \n
s - para sul \n
n - para norte\n\n""")

ano = input("\nO ano é bissexto? (s ou n): ")

is_bissexto = False

if ano == "s":
    is_bissexto = True

if hemisferio == "s":
    if mes == 10 or mes == 11:
        print("\nPrimavera")

    elif mes == 1 or mes == 2:
        print("\nVerão")

    elif mes == 4 or mes == 5:
        print("\nOutono")

    elif mes == 7 or mes == 8:
        print("\nInverno")

    elif mes == 9:
        if is_bissexto:
            if dia >= 21:
                print("\nPrimavera")

            else:
                print("\nInverno")

        else:
            if dia >= 22:
                print("\nPrimavera")

            else:
                print("\nInverno")

    elif mes == 12:
        if is_bissexto:
            if dia <= 20:
                print("\nPrimavera")

            else:
                print("\nVerão")

        else:   
            if dia <= 21:
                print("\nPrimavera")

            else:
                print("\nVerão")

    elif mes == 3:
        if is_bissexto:
            if dia <= 20:
                print("\nVerão")

            else:
                print("\nOutono")

        else:   
            if dia <= 21:
                print("\nVerão")

            else:
                print("\nOutono")

    elif mes == 6:
        if is_bissexto:
           if dia <= 20:
                print("\nOutono")
           else:
               print("\nInverno")

        else:
            if dia <= 21:
                print("\nOutono")

            else:
                print("\nInverno")

else:
    if mes == 10 or mes == 11:
        print("\nOutono")

    elif mes == 1 or mes == 2:
        print("\nInverno")

    elif mes == 4 or mes == 5:
        print("\nPrimavera")

    elif mes == 7 or mes == 8:
        print("\nVerão")

    elif mes == 9:
        if is_bissexto:
            if dia >= 21:
                print("\nOutono")

            else:
                print("\nVerão")
                
        else:
            if dia >= 22:
                print("\nOutono")

            else:
                print("\nVerão")

    elif mes == 12:
        if is_bissexto:
            if dia <= 20:
                print("\nOutono")

            else:
                print("\nInverno")

        else:
            if dia <= 21:
                print("\nOutono")

            else:
                print("\nInverno")

    elif mes == 3:
        if is_bissexto:
            if dia <= 20:
                print("\nInverno")

            else:
                print("\nPrimavera")

        else:
            if dia <= 21:
                print("\nInverno")

            else:
                print("\nPrimavera")

    elif mes == 6:
        if is_bissexto:
            if dia <= 20:
                print("\nPrimavera")

            else:
                print("\nVerão")
        else:
            if dia <= 21:
                print("\nPrimavera")

            else:
                print("\nVerão")
            
