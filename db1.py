from pymongo import MongoClient
from bson.objectid import ObjectId
import db3

uri = "seu uri"
client = MongoClient(uri)
db = client['NomeBanco']
collection = db['Corridas']

def cadastrar_corrida():
    nome = str(input("Nome da corrida: "))
    categoria = str(input("Categoria (F1, NASCAR ou MotoGP):"))
    dia = int(input("Dia da corrida: "))
    mes = int(input("Mês da corrida: "))
    ano = int(input("Ano da corrida: "))
    horario_inical = str(input("Horário de inicio da corrida: "))
    local = str(input("Local da corrida: "))
    qtd_pilotos = int(input("Quantidade de pilotos participantes: "))
    qtd_ingressos = int(input("Quantidade total de ingressos: "))
    valor_ingresso = float(input("Valor do ingreso: "))
    if(categoria == "F1"):
        qtd_voltas = int(input("Qual a quantidade de voltas da corrida:"))
        collection.insert_one({"nome_corrida": nome, "categoria": categoria, "dia_corrida": dia, "mes_corrida" : mes, "ano_corrida": ano, "horario_inical": horario_inical, "local": local, "qtd_pilotos": qtd_pilotos, "qtd_ingressos": qtd_ingressos, "valor_ingresso": valor_ingresso, "qtd_voltas": qtd_voltas})
    elif(categoria =="NASCAR"):
        tipo_pista = str(input("Qual o tipo de pista: "))
        collection.insert_one({"nome_corrida": nome, "categoria": categoria, "dia_corrida": dia, "mes_corrida" : mes, "ano_corrida": ano, "horario_inical": horario_inical, "local": local, "qtd_pilotos": qtd_pilotos, "qtd_ingressos": qtd_ingressos, "valor_ingresso": valor_ingresso, "tipo_pista": tipo_pista})
    elif(categoria == "MotoGP"):
        cilindrada = str(input("Qual a cilindrada máxima: "))
        collection.insert_one({"nome_corrida": nome, "categoria": categoria, "dia_corrida": dia, "mes_corrida" : mes, "ano_corrida": ano, "horario_inical": horario_inical, "local": local, "qtd_pilotos": qtd_pilotos, "qtd_ingressos": qtd_ingressos, "valor_ingresso": valor_ingresso, "cilindrada": cilindrada})
    else:
        print("Categoria inválida")
        return 0
    print("Nova corrida cadastrada com sucesso!\n")

def deletar_corrida():
    deletar_nome = str(input("Digite o nome da corrida que deseja deletar: "))
    print(f"Tem certeza que deseja deletar a corrida {deletar_nome}? Não pode ser desfeito!")
    deletar = str(input())
    if(deletar == "Sim" or deletar == "sim"):
        collection.delete_one({"nome_corrida": deletar_nome})
        print("Corrida deletada com sucesso!\n")

def atualizar_corrida():
    atualizar_nome = str(input("Digite o nome da corrida que deseja atualizar: "))
    print("1 - Atualizar data")
    print("2 - Atualizar local")
    print("3 - Atualizar quantidade de pilotos")
    print("4 - Atualizar quantidade de ingressos")
    print("5 - Atualizar valor do ingresso")
    atualizar_opcao = int(input("O que deseja atualizar: "))
    if(atualizar_opcao == 1):
        atualizar_dado_dia = int(input("Digite o dia atualizado: "))
        atualizar_dado_mes = int(input("Digite o mes atualizado: "))
        atualizar_dado_ano = int(input("Digite o ano atualizado: "))
        collection.update_one({"nome_corrida": atualizar_nome}, {"$set": {"dia_corrida": atualizar_dado_dia}})
        collection.update_one({"nome_corrida": atualizar_nome}, {"$set": {"mes_corrida": atualizar_dado_mes}})
        collection.update_one({"nome_corrida": atualizar_nome}, {"$set": {"ano_corrida": atualizar_dado_ano}})
        print("Data atualizada!")
    elif(atualizar_opcao == 2):
        atualizar_dado = str(input("Digite o local atualizado: "))
        collection.update_one({"nome_corrida": atualizar_nome}, {"$set": {"local": atualizar_dado}})
        print("Local atualizado!")
    elif(atualizar_opcao == 3):
        atualizar_dado = int(input("Digite a quantidade de pilotos atualizada: "))
        collection.update_one({"nome_corrida": atualizar_nome}, {"$set": {"qtd_pilotos": atualizar_dado}})
        print("Quantidade de pilotos atualizada!")
    elif(atualizar_opcao == 4):
        atualizar_dado = int(input("Digite a quantidade de ingressos atualizada: "))
        collection.update_one({"nome_corrida": atualizar_nome}, {"$set": {"qtd_ingressos": atualizar_dado}})
        print("Quantidade de ingressos atualizada!")
    elif(atualizar_opcao == 5):
        atualizar_dado = float(input("Digite o valor atualizado: "))
        collection.update_one({"nome_corrida": atualizar_nome}, {"$set": {"valor_ingresso": atualizar_dado}})
        print("Valor atualizado!")
    else:
        print("inválido")

def listar_corridas():
    todas_corridas = collection.find()
    num_corrida = 0
    for corrida in todas_corridas:
        num_corrida += 1
        if(corrida['categoria'] == "F1"):
            print(f"\n Corrida {num_corrida}\n Nome da corrida: {corrida['nome_corrida']}\n Categoria: {corrida['categoria']}\n Data da corrida: {corrida['dia_corrida']}/{corrida['mes_corrida']}/{corrida['ano_corrida']}\n Local: {corrida['local']}\n Quantidade de pilotos: {corrida['qtd_pilotos']}\n Quantidade de ingressos disponiveis: {corrida['qtd_ingressos']}\n Valor do ingresso: {corrida['valor_ingresso']}\n Quantidade de voltas: {corrida['qtd_voltas']}\n\n")
        elif(corrida['categoria'] == "NASCAR"):
            print(f"\n Corrida {num_corrida}\n Nome da corrida: {corrida['nome_corrida']}\n Categoria: {corrida['categoria']}\n Data da corrida: {corrida['dia_corrida']}/{corrida['mes_corrida']}/{corrida['ano_corrida']}\n Local: {corrida['local']}\n Quantidade de pilotos: {corrida['qtd_pilotos']}\n Quantidade de ingressos disponiveis: {corrida['qtd_ingressos']}\n Valor do ingresso: {corrida['valor_ingresso']}\n Tipo de pista: {corrida['tipo_pista']}\n\n")
        elif(corrida['categoria'] == "MotoGP"):
            print(f"\n Corrida {num_corrida}\n Nome da corrida: {corrida['nome_corrida']}\n Categoria: {corrida['categoria']}\n Data da corrida: {corrida['dia_corrida']}/{corrida['mes_corrida']}/{corrida['ano_corrida']}\n Local: {corrida['local']}\n Quantidade de pilotos: {corrida['qtd_pilotos']}\n Quantidade de ingressos disponiveis: {corrida['qtd_ingressos']}\n Valor do ingresso: {corrida['valor_ingresso']}\n Cilindrada máxima: {corrida['cilindrada']}\n\n")

def selecionar_corrida(id_usuario):
    nome_buscar = str(input("Digite o nome da corrida que deseja selecionar: "))
    corrida = collection.find_one({"nome_corrida": nome_buscar})
    if(corrida['categoria'] == "F1"):
        print(f"\n Nome da corrida: {corrida['nome_corrida']}\n Categoria: {corrida['categoria']}\n Data da corrida: {corrida['dia_corrida']}/{corrida['mes_corrida']}/{corrida['ano_corrida']}\n Local: {corrida['local']}\n Quantidade de pilotos: {corrida['qtd_pilotos']}\n Quantidade de ingressos disponiveis: {corrida['qtd_ingressos']}\n Valor do ingresso: {corrida['valor_ingresso']}\n Quantidade de voltas: {corrida['qtd_voltas']}\n\n")
    elif(corrida['categoria'] == "NASCAR"):
        print(f"\n Nome da corrida: {corrida['nome_corrida']}\n Categoria: {corrida['categoria']}\n Data da corrida: {corrida['dia_corrida']}/{corrida['mes_corrida']}/{corrida['ano_corrida']}\n Local: {corrida['local']}\n Quantidade de pilotos: {corrida['qtd_pilotos']}\n Quantidade de ingressos disponiveis: {corrida['qtd_ingressos']}\n Valor do ingresso: {corrida['valor_ingresso']}\n Tipo de pista: {corrida['tipo_pista']}\n\n")
    elif(corrida['categoria'] == "MotoGP"):
        print(f"\n Nome da corrida: {corrida['nome_corrida']}\n Categoria: {corrida['categoria']}\n Data da corrida: {corrida['dia_corrida']}/{corrida['mes_corrida']}/{corrida['ano_corrida']}\n Local: {corrida['local']}\n Quantidade de pilotos: {corrida['qtd_pilotos']}\n Quantidade de ingressos disponiveis: {corrida['qtd_ingressos']}\n Valor do ingresso: {corrida['valor_ingresso']}\n Cilindrada máxima: {corrida['cilindrada']}\n\n")
    selecionar = str(input(f"Deseja selecionar a corrida {nome_buscar}?"))
    if(selecionar == "Sim" or selecionar == "sim"):
        db3.adicionarCarrinho(id_usuario, corrida["_id"], corrida['nome_corrida'], corrida['categoria'], corrida['valor_ingresso'])

def diminuirIngresso(id_corrida, qtd_ingressos):
    corrida = collection.find_one({"_id": ObjectId(id_corrida)})
    nova_qtd = corrida['qtd_ingressos'] - qtd_ingressos
    collection.update_one({"_id": ObjectId(id_corrida)}, {"$set": {"qtd_ingressos": nova_qtd}})

def buscar_corrida(nome_corrida):
    corrida = collection.find_one({"nome_corrida": nome_corrida})
    if not corrida:
        return "Não encontrado"
    corrida["_id"] = str(corrida["_id"])
    return corrida

def valor_corrida(nome_corrida):
    corrida = collection.find_one({"nome_corrida": nome_corrida})
    if not corrida:
        return "Não encontrado"
    return corrida["valor_ingresso"]

def close_client():
    client.close()
