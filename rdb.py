from supabase import create_client

url_supa = "seu url"
key_supa = "sua chave"
supabase = create_client(url_supa, key_supa)

def cadastro_usuario(nome, sobrenome, email, senha, cpf, tipo):
    if(tipo == "Cliente"):
        telefone = str(input("Telefone: "))
        dia_nascimento = int(input("Dia de nascimento: "))
        mes_nascimento = int(input("Mês de nascimento: "))
        ano_nascimento = int(input("Ano de nascimento: "))
    elif(tipo == "Administrador"):
        cargo = str(input("Cargo: "))
        salario = float(input("Salário: "))
    novo_usuario = supabase.table("usuários").insert(
        {
            "nome_usuario": nome,
            "sobrenome_usuario": sobrenome,
            "email": email,
            "senha": senha,
            "cpf": cpf,
        }
    ).execute()
    id_usuario = novo_usuario.data[0]["id_usuario"]
    if(tipo == "Cliente"):
        supabase.table("clientes").insert(
            {
                "id_usuario": id_usuario,
                "telefone": telefone,
                "dia_nascimento": dia_nascimento,
                "mes_nascimento": mes_nascimento,
                "ano_nascimento": ano_nascimento,
            }
        ).execute()
    elif(tipo == "Administrador"):
        supabase.table("administradores").insert(
            {
                "id_usuario": id_usuario,
                "cargo": cargo,
                "salario": salario,
            }
        ).execute()
    return id_usuario

def login_usuario(email, senha):
    verificar = supabase.table("usuários").select("*").eq("email", email).eq("senha", senha).execute()
    if verificar.data:
        return verificar.data[0]
    else:
        return None

def deletar_conta(email_conta):
    print(f"Tem certeza que deseja deletar a conta? Não pode ser desfeito!")
    deletar = str(input())
    if(deletar == "Sim" or deletar == "sim"):
        supabase.table("usuários").delete().eq("email", email_conta).execute()
        print("Conta deletada com sucesso!\n")

def atualizar_conta(email_conta, id_usuario):
    print("1 - Atualizar telefone")
    print("2 - Atualizar senha")
    print("3 - Atualizar CPF")
    atualizar_opcao = int(input("O que deseja atualizar: "))
    if(atualizar_opcao == 1):
        atualizar_dado = str(input("Novo telefone: "))
        supabase.table("clientes").update({"telefone": atualizar_dado}).eq("id_usuario", id_usuario).execute()
        print("Telefone atualizado!")
    elif(atualizar_opcao == 2):
        atualizar_dado = int(input("Nova senha "))
        supabase.table("usuários").update({"senha": atualizar_dado}).eq("email", email_conta).execute()
        print("Senha atualizada!")
    elif(atualizar_opcao == 3):
        atualizar_dado = str(input("Novo CPF: "))
        supabase.table("corridas").update({"cpf": atualizar_dado}).eq("email", email_conta).execute()
        print("CPF atualizado!")

def verificar_perfil(email_conta, id_usuario):
    info_cliente = supabase.table("usuários").select("*").eq("email", email_conta).execute()
    info_cliente = info_cliente.data[0]
    print(f"\nNome: {info_cliente['nome_usuario']} {info_cliente['sobrenome_usuario']}\n E-mail: {info_cliente['email']}\n CPF: {info_cliente['cpf']}")
    info_cliente = supabase.table("clientes").select("*").eq("id_usuario", id_usuario).execute()
    info_cliente = info_cliente.data[0]
    print(f"Telefone: {info_cliente['telefone']}\n Data de nascimento: {info_cliente['dia_nascimento']}/{info_cliente['mes_nascimento']}/{info_cliente['ano_nascimento']}\n")
    print("1 - Atualizar perfil\n")
    print("2 - Deletar conta\n")
    print("0 - Voltar\n")
    opcao_perfil = int(input())
    if(opcao_perfil == 1):
        atualizar_conta(email_conta, id_usuario)
    elif(opcao_perfil == 2):
        deletar_conta(email_conta)
        return 1
    elif(opcao_perfil == 0):
        return 0
    else:
        print("Inválido")

def listar_clientes():
    clientes = supabase.table("clientes").select("*").execute()
    for cliente in clientes.data:
        id_usuario = cliente["id_usuario"]
        cliente_dados = supabase.table("usuários").select("*").eq("id_usuario", id_usuario).execute()
        cliente_dados = cliente_dados.data[0]
        print(f"\nNome: {cliente_dados['nome_usuario']} {cliente_dados['sobrenome_usuario']}\n E-mail: {cliente_dados['email']}\n CPF: {cliente_dados['cpf']}\n Telefone: {cliente['telefone']}\n Data de nascimento: {cliente['dia_nascimento']}/{cliente['mes_nascimento']}/{cliente['ano_nascimento']}")
