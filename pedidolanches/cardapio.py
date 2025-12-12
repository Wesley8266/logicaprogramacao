from tabulate import tabulate

def carregar_cardapio():
    cardapio = [ 
    {"id": 1, "nome": "Hambúrguer", "preco": 12.50}, 
    {"id": 2, "nome": "Batata Frita", "preco": 7.00}, 
    {"id": 3, "nome": "Refrigerante", "preco": 5.00} 
    ]
    return cardapio

def exibir_cardapio(cardapio):
    print(carregar_cardapio)

def buscar_item(cardapio, id_item):
    item = []
    buscar = int(input("id do produto: "))
    for i in cardapio:
        if buscar == i["id"]:
            item.append(i)
        elif i != i["id"]:
            print("nenhum produto encontrado!")
    print(tabulate([item], headers = "keys", tablefmt = "fancy_grid"))



