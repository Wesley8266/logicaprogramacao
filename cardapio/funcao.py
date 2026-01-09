from tabulate import tabulate

def carregar_cardapio():
    return [
        {"id": 1, "nome": "Hambúrguer", "preco": 12.5},
        {"id": 2, "nome": "Pizza", "preco": 30},
        {"id": 3, "nome": "Refrigerante", "preco": 5}
    ]


def exibir_cardapio(cardapio):
    tabela = []
    for item in cardapio:
        tabela.append([item["id"], item["nome"], item["preco"]])

    print(tabulate(tabela, headers=["ID", "Nome", "Preço"], tablefmt="fancy_grid"))


def adicionar_pedido(cardapio, pedido):
    id_item = int(input("ID do item: "))
    qtd = int(input("Quantidade: "))

    for item in cardapio:
        if item["id"] == id_item:
            pedido.append({
                "id": item["id"],
                "nome": item["nome"],
                "qtd": qtd,
                "total": item["preco"] * qtd
            })


def exibir_pedido(pedido):
    tabela = []
    total = 0

    for p in pedido:
        tabela.append([p["id"], p["nome"], p["qtd"], p["total"]])
        total += p["total"]

    print(tabulate(tabela, headers=["ID", "Item", "Qtd", "Total"], tablefmt="grid"))
    print("Total da compra:", total)


def remover_item(pedido):
    id_item = int(input("ID para remover: "))

    for p in pedido:
        if p["id"] == id_item:
            pedido.remove(p)
            break
