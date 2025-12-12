from tabulate import tabulate


def carregar_cardapio(listacardapio):
    lista = {"id": 1, "nome": "Hambúrguer", "preco": 12.5, "id": 2, "nome": "Pizza", "preco": 30, "id": 3, "nome": "Refrigerante", "preco": 5}
    listacardapio.append(lista)
    return listacardapio

def exibir_cardapio(carregar_cardapio):
    tabela = []
    for i in carregar_cardapio:
        tabela.append([i["id"], i["nome"], i["preco"]])
    print(tabulate(
        tabela, 
        headers= ["id","nome","preco"], tablefmt = "fancy_grid"))



def adicionar_pedido(listacardapio):
    pedido = []
    item = input("id: ")

def exibir_pedido(pedido):
    return pedido


def remover_pedido(listapedido):
    re=input("Qual pedido deseja remover? ")
    for i in listapedido:
        if re==i["id"]:
            listapedido.remove(re)



