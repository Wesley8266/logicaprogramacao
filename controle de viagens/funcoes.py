from tabulate import tabulate


def registrar_viagens(listaviagens):
    motorista = input("nome do motorista:")
    destino = input("destino: ")
    distancia = float(input("distancia em km: "))
    gasto_combustivel  =float(input( "Valor gasto com combustível(em R$):"))
    consumo = gasto_combustivel / distancia
    viagem = {"motorista": motorista, "destino": destino, "distancia":distancia, "gasto_combustivel": gasto_combustivel, "consumo": consumo}
    listaviagens.append(viagem)
    return viagem

def exibir_viagens(listaviagens):
    tabela = []
    for i in listaviagens:
        tabela.append([i["motorista"], i["destino"], i["distancia"], i["gasto_combustivel"], i["consumo"]])
    print(tabulate(
        tabela, 
        headers= ["motorista","destino","distancia","gasto_combustivel","consumo"], tablefmt = "fancy_grid"))



def buscar_motorista(listaviagens):
    viagem_m = []
    motorista = input("qual motorista deseja consultar: ")
    for i in listaviagens:
        if motorista == i["motorista"]:
            viagem_m.append(([i["motorista"], i["destino"], i["distancia"], i["gasto_combustivel"], i["consumo"]]))
    print(tabulate(
        viagem_m, 
        headers= ["motorista","destino","distancia","gasto_combustivel","consumo"], tablefmt = "fancy_grid"))



def viagem_mais_cara(listaviagens):
    from tabulate import tabulate

def viagem_mais_cara(lista_viagens):
    maior = None
    viagem_mais_cara = None

    for viagem in lista_viagens:
        if maior is None or viagem["gasto_combustivel"] > maior:
            maior = viagem["gasto_combustivel"]
            viagem_mais_cara = viagem

    lista_m = [[
        viagem_mais_cara["motorista"],
        viagem_mais_cara["destino"],
        viagem_mais_cara["distancia"],
        viagem_mais_cara["gasto_combustivel"],
        viagem_mais_cara["consumo"]
    ]]

    print(tabulate(
        lista_m,
        headers=["motorista", "destino", "distancia", "gasto_combustivel", "consumo"],
        tablefmt="fancy_grid"
    ))


def media_consumo(listaviagens):
    soma = 0
    for viagem in listaviagens:
        soma += viagem["consumo"]
    media = soma / len(listaviagens)
    return f"consumo geral das viagens: {media}"
        