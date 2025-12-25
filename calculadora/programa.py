from operacoes import *

print("1-soma-------------------")
print("2-subtraçao")
print("3-multiplicaçao")
print("4-divisao")
print("0-sair____________________")


while True:
    operacao= input("realizar operaçao: ")
    if operacao == "0":
        print("programa encerrado! ")
        break
    a = float(input("digite o 1° numero: "))
    b = float(input("digite o 2° numero: "))
    
    if operacao == "1":
        print(soma(a,b))
    elif operacao == "2":
        print(subtracao(a,b))
    elif operacao == "3":
        print(multiplicacao(a,b))
    elif operacao == "4":
        print(divisao(a,b))




