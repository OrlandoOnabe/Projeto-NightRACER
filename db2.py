from cassandra.cluster import Cluster
from datetime import datetime
import uuid
import db1
import db3

cluster = Cluster(['127.0.0.1']) 
session = cluster.connect()
session.set_keyspace('nightracer')

def registrarPedido(id_usuario, id_corrida, nome_corrida, categoria, qtd_ingresso, valor):
    id_pedido = uuid.uuid4()
    data_pedido = datetime.now()
    session.execute(
        "INSERT INTO pedidos (id_pedido, data_pedido, id_usuario, id_corrida, nome_corrida, categoria, qtd_ingressos, valor_pedido, tipo_pagamento, status_pedido) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (id_pedido, data_pedido, id_usuario, id_corrida, nome_corrida, categoria, qtd_ingresso, valor, "NENHUM", "PENDENTE")
    )
    realizarPagamento(id_usuario, id_corrida, data_pedido, qtd_ingresso)

def realizarPagamento(id_usuario, id_corrida, data_pedido, qtd_ingressos):
    print("Qual metodo de pagamento:\n")
    print("1 - Crédito\n")
    print("2 - PIX\n")
    print("0 - Cancelar compra\n")
    metodo = int(input())
    if(metodo == 1):
        pagamento = "Crédito"
        session.execute(
            "UPDATE pedidos SET tipo_pagamento = %s, status_pedido = %s WHERE id_usuario = %s AND data_pedido = %s",
            (pagamento, "PAGO", id_usuario, data_pedido)
        )
        print("Pagamento realizado!\n")
        db1.diminuirIngresso(id_corrida, qtd_ingressos)
        db3.limparCarrinho(id_usuario)
    elif(metodo == 2):
        pagamento = "PIX"
        session.execute(
            "UPDATE pedidos SET tipo_pagamento = %s, status_pedido = %s WHERE id_usuario = %s AND data_pedido = %s",
            (pagamento, "PAGO", id_usuario, data_pedido)
        )
        print("Pagamento realizado!\n")
        db1.diminuirIngresso(id_corrida, qtd_ingressos)
        db3.limparCarrinho(id_usuario)
    elif(metodo == 0):
        cancelarPedido(id_usuario, data_pedido)
    else:
        print("Inválido")
        return 0


def cancelarPedido(id_usuario, data_pedido):
    session.execute(
        "DELETE FROM pedidos WHERE id_usuario = %s AND data_pedido = %s",
        (id_usuario, data_pedido)
    )
    print("Pedido cancelado!\n")

def listarCompras(id_usuario):
    compras = session.execute(
        "SELECT * FROM pedidos WHERE id_usuario = %s",
        (id_usuario,)
    )
    if not compras.one():
        print("Vázio")
        return 0
    for pedido in compras:
        print(f"\nCorrida:{pedido.nome_corrida}\n Quantidade de ingressos {pedido.qtd_ingressos}\n Valor da compra: {pedido.valor_pedido}\n")
