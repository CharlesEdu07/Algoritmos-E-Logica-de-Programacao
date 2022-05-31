from datetime import date

data_atual = date.today()

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

dia_temp, mes_temp, ano_temp = data_em_texto.split("/")
dia_atual, mes_atual, ano_atual = int(dia_temp), int(mes_temp), int(ano_temp)

data_nas = input("Digite sua data de nascimento (dd/mm/aa): ")

dia_temp, mes_temp, ano_temp = data_nas.split("/")

dia_nas, mes_nas, ano_nas = int(dia_temp), int(mes_temp), int(ano_temp)

idade = ano_atual - ano_nas

if mes_atual > mes_nas:
    print("Você tem", idade, "anos e já fez aniversário esse ano")

elif mes_atual < mes_nas:
    print("Você tem", idade - 1, "anos e ainda fará aniversário esse ano")

else:
    if dia_atual > dia_nas:
        print("Você tem", idade, "anos e já fez aniversário esse ano")

    elif dia_atual < dia_nas:
        print("Você tem", idade - 1, "anos e ainda fará aniversário esse ano")

    else:
        print("Parabéns! Você faz", idade, "anos hoje")

    

