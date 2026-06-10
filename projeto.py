import rdb
import db1
import db2
import db3

def menu_cliente(email_conta, id_cliente):
    while True:
        print("\nNightRACER\n")
        print("1 - Verificar corridas\n")
        print("2 - Selecionar corrida\n")
        print("3 - Verificar carrinho\n")
        print("4 - Verificar perfil\n")
        print("5 - Histórico de compras\n")
        print("0 - Logout\n")
        opcao_cliente = int(input())
        if(opcao_cliente == 1):
            db1.listar_corridas()
        elif(opcao_cliente == 2):
            db1.selecionar_corrida(id_cliente)
        elif(opcao_cliente == 3):
            db3.verificarCarrinho(id_cliente)
        elif(opcao_cliente == 4):
            verificar = rdb.verificar_perfil(email_conta, id_cliente)
            if(verificar == 1):
                break
        elif(opcao_cliente == 5):
            db2.listarCompras(id_cliente)
        elif(opcao_cliente == 0):
            print("Deslogando...\n")
            break
        else:
            print("Inválido")

def menu_administrador(email_conta):
    while True:
        print("NightRACER\n")
        print("\n1 - Cadastrar corrida\n")
        print("2 - Listar corridas\n")
        print("3 - Cancelar corrida\n")
        print("4 - Atualizar corrida\n")
        print("5 - Listar clientes\n")
        print("0 - Logout\n")
        opcao_adm = int(input("Qual opção deseja: "))
        if(opcao_adm == 1):
            db1.cadastrar_corrida()
        elif(opcao_adm == 2):
            db1.listar_corridas()
        elif(opcao_adm == 3):
            db1.deletar_corrida()
        elif(opcao_adm == 4):
            db1.atualizar_corrida()
        elif(opcao_adm == 5):
            rdb.listar_clientes()
        elif(opcao_adm == 0):
            print("Deslogando...\n")
            break
        else:
            print("Inválido")

def cadastro_usuario():
    print("Escolha o tipo de cadastro\n")
    print("1 - Cliente\n")
    print("2 - Administrador\n")
    cadastro_opcao = int(input())
    if(cadastro_opcao == 1):
        tipo_usuario = "Cliente"
    elif(cadastro_opcao == 2):
        tipo_usuario = "Administrador"
    else:
        return "Inválido"
    nome_usuario = str(input("Nome: "))
    sobrenome_usuario = str(input("Sobrenome: "))
    email_usuario = str(input("E-mail: "))
    senha_usuario = str(input("Senha: "))
    cpf_usuario = str(input("CPF: "))
    id_usuario = rdb.cadastro_usuario(nome_usuario, sobrenome_usuario, email_usuario, senha_usuario, cpf_usuario, tipo_usuario)
    print("Cadastro realizado com sucesso!\n")
    if(tipo_usuario == "Cliente"):
        menu_cliente(email_usuario, id_usuario)
    elif(tipo_usuario == "Administrador"):
        menu_administrador(email_usuario)

def login_usuario():
    print("Escolha o tipo de login\n")
    print("1 - Cliente\n")
    print("2 - Administrador\n")
    login_opcao = int(input())
    if(login_opcao == 1):
        tipo_usuario = "Cliente"
    elif(login_opcao == 2):
        tipo_usuario = "Administrador"
    else:
        return "Inválido"
    email_usuario = str(input("E-mail: "))
    senha_usuario = str(input("Senha: "))
    verificar = rdb.login_usuario(email_usuario, senha_usuario)
    if(verificar):
        id_usuario = verificar["id_usuario"]
        print("Login realizado com sucesso!\n")
        if(tipo_usuario == "Cliente"):
            menu_cliente(email_usuario, id_usuario)
        if(tipo_usuario == "Administrador"):
            menu_administrador(email_usuario)
    else:
        print("Login inválido\n")

while True:
    print("NightRACER\n")
    print("1 - Login\n")
    print("2 - Cadastro\n")
    print("0 - Sair\n")
    opcao = int(input())
    if(opcao == 1):
        login_usuario()
    elif(opcao == 2):
        cadastro_usuario()
    elif(opcao == 0):
        db1.close_client()
        break
    else:
        print("\nopção inexistente\n")
