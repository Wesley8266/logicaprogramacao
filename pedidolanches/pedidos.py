from cardapio import *

def novo_pedido(cardapio):
    id = 1
    pedido = []
    item = input("id do item: ")
    for i in cardapio:
        while True:
            novo = input("adicionar novo pedido?")
            if novo == "adicionar":
                if item == i["id"]:
                    preco = i["preco"]
                    quantidade = int(input("quantidade: "))
                    subtotal = preco * quantidade
                    resultado = {
                    "id": id,
                    "item": i["id"],
                    "quantidade": quantidade,
                    "total": subtotal
                }
                    pedido.append(resultado)
                    id += 1
                return pedido

def calcular_total(pedido, cardapio, subtotal):
    total = 0
    for i in pedido:
        total += i["total"]
        if total > 50:
            desconto = (subtotal / total) * 100
            print(desconto)
            total.append(total)
            for i  in pedido:
                if i["id"] >= 5:
                    print("voce ganhou um brinde!")


