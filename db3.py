import redis
import db2
import db1

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def adicionarCarrinho(id_usuario, id_corrida, nome_corrida, categoria, valor):
    chave = f"carrinho:usuario{id_usuario}:corrida{id_corrida}"
    qtd_ingressos = int(input("Quantos ingressos deseja: "))
    valor = valor * qtd_ingressos
    r.hset(chave, mapping={
        "nome_corrida": nome_corrida,
        "categoria": categoria,
        "qtd_ingressos": qtd_ingressos,
        "valor": valor
    })
    print("Adicionado ao carrinho!\n")
    r.expire(chave, 600)

def verificarCarrinho(id_usuario):
    valor_total = 0
    chave = f"carrinho:usuario{id_usuario}:corrida*"
    verificar = r.keys(chave)
    carrinho_pedidos = []
    if not verificar:
        print("Carrinho vázio\n")
        return 0
    for c in verificar:
        carrinho = r.hgetall(c)
        id_corrida = c.split("corrida")[1]
        carrinho_pedidos.append({"id_corrida": id_corrida, "pedido": carrinho})
        valor_total += float(carrinho['valor'])
        print(f"Corrida: {carrinho['nome_corrida']}  Categoria : {carrinho['categoria']}\n Quantidade: {carrinho['qtd_ingressos']}\n Valor: {carrinho['valor']}\n")
    print("Valor total: ", valor_total)
    print("\n1 - Confirmar pedido")
    print("\n2 - Remover item")
    print("\n3 - Atualizar item")
    print("\n0 - Voltar\n")
    opcao_carrinho = int(input())
    if(opcao_carrinho == 1):
        for pedido in carrinho_pedidos:
            db2.registrarPedido(id_usuario, pedido['id_corrida'], pedido['pedido']['nome_corrida'], pedido['pedido']['categoria'], int(pedido['pedido']['qtd_ingressos']), float(pedido['pedido']['valor']))
    elif(opcao_carrinho == 2):
        removerCarrinho(id_usuario)
    elif(opcao_carrinho == 3):
        atualizarCarrinho(id_usuario)
    elif(opcao_carrinho == 0):
        return 0
    else:
        print("Inválido")

def atualizarCarrinho(id_usuario):
    print("Deseja atualizar em qual corrida: ")
    nome_atualizar = str(input())
    corrida = db1.buscar_corrida(nome_atualizar)
    id_corrida = corrida["_id"]
    chave = f"carrinho:usuario{id_usuario}:corrida{id_corrida}"
    qtd_ingressos = int(input("Quantos ingressos deseja: "))
    valor = db1.valor_corrida(nome_atualizar)
    valor = valor * qtd_ingressos
    r.hset(chave, "qtd_ingressos", qtd_ingressos)
    r.hset(chave, "valor", valor)
    verificarCarrinho(id_usuario)

def removerCarrinho(id_usuario):
    print("Deseja deletar qual corrida do carrinho: ")
    nome_deletar = str(input())
    corrida = db1.buscar_corrida(nome_deletar)
    id_corrida = corrida["_id"]
    chave = f"carrinho:usuario{id_usuario}:corrida{id_corrida}"
    r.delete(chave)
    verificarCarrinho(id_usuario)

def limparCarrinho(id_usuario):
    chaves = f"carrinho:usuario{id_usuario}:corrida*"
    deletar = r.keys(chaves)
    r.delete(*deletar)
