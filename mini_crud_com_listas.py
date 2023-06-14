import datetime

name_list = []
email_list = []
tel_list = []
birthday_list = []

def create(data):
    name_list.append(data["name"])
    email_list.append(data["email"])
    tel_list.append(data["tel"])
    birthday_list.append(data["birthday"])

def show():
    data_st = []
    formated_data = []
    
    for i in range(len(name_list)):
        data_st += "\n" + str(i+1) + " - Name: " + name_list[i], "Email: " + email_list[i], "Telefone: " + tel_list[i], "Data de nascimento: " + birthday_list[i]

    formated_data = "\t".join(data_st)
        
    return formated_data

def search(value):
    value_index = 0
    
    if value in name_list:
        value_index = name_list.index(value)
    
    elif value in email_list:
        value_index = email_list.index(value)

    elif value in tel_list:
        value_index = tel_list.index(value)

    elif value in birthday:
        value_index = birthday_list.index(value)

    else:
        return "Nenhum dado encontrado"

    data_st = "\nName: " + name_list[value_index], "Email: " + email_list[value_index], "Telefone: " + tel_list[value_index], "Data de nascimento: " + birthday_list[value_index]

    formated_data = "\t".join(data_st)

    return formated_data

def delete(index):
    del name_list[index]
    del email_list[index]
    del tel_list[index]
    del birthday_list[index]

def update(data, index):
    name_list[index] = data["name"]
    email_list[index] = data["email"]
    tel_list[index] = data["tel"]
    birthday_list[index] = data["birthday"]

op = "s"

data = []

data_st = []
formated_data = []

while op == "s":
    print()
    print("-------------------------------")
    print("----------- Agenda ------------")
    print("-------------------------------")
    print("\nO que deseja fazer?")
    print("\n1 - Criar dados")
    print("2 - Consultar dados")
    print("3 - Pesquisar dados")
    print("4 - Apagar")
    print("5 - Atualizar")
    print("0 - Sair")

    op2 = input("\nDigite: ")

    if op2 == "1":
        print("\nCriando dado...")

        name = input("Digite o nome: ")
        email = input("Digite o email: ")
        tel = input("Digite o telefone: ")
        birthday = input("Digite a data de nascimento (dd/mm/aa): ")

        data = {
            "name": name,
            "email": email,
            "tel": tel,
            "birthday": birthday
        }

        create(data)

        print("\nDado criado!")

    elif op2 == "2":
        print("\nMostrando todos os dados:")

        print(show())

        print("\nTodos os dados consultados")

    elif op2 == "3":
        print("\nPesquisando um dado: ")

        value = input("\nDigite o valor para pesquisar: ")
    
        print(search(value))

        print("Encerrando busca")

    elif op2 == "4":
        if name_list:
            print("\nDeletando dado...")
            print(show())

            index = int(input("\nDigite o dado que deseja excluir: "))
            
            if index <= len(name_list):
                index -= 1
                
                delete(index)

                print("\nDado deletado")

            else:
                ("\nOpção inválida")

            print(show())

        else:
            print("\nA lista de dados está vazia")

    elif op2 == "5":
        print("\nEditando dado...")
    
        print(show())

        index = int(input("\nDigite o dado que deseja atualizar: "))

        if index <= len(name_list):
            print("\nAtualizando dado: ")

            name = input("Digite o novo nome: ")
            email = input("Digite o novo email: ")
            tel = input("Digite o novo telefone: ")
            birthday = input("Digite a nova data de nascimento (dd/mm/aa): ")

            data = {
                "name": name,
                "email": email,
                "tel": tel,
                "birthday": birthday
            }

            index -= 1
            
            update(data, index)

            print("\nDado atualizado")

        else:
            ("\nOpção inválida")

    else:
        print("\nSaindo...")

        op = "n"
        
