from funcao import *

cardapio = carregar_cardapio()
pedido = []

print("1 - Ver cardápio")
print("2 - Adicionar item")
print("3 - Ver pedido")
print("4 - Remover item")
print("0 - Sair")
while True:

    op = input("Opção: ")

    if op == "1":
        exibir_cardapio(cardapio)

    elif op == "2":
        exibir_cardapio(cardapio)
        adicionar_pedido(cardapio, pedido)

    elif op == "3":
        exibir_pedido(pedido)

    elif op == "4":
        remover_item(pedido)

    elif op == "0":
        break
