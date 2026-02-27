import random as rd

print("-----------------------------")
print("\nBem vindo ao jogo de ADIVINHA\n")
print("-----------------------------")

#definir a variavel
n_tentativas = 0
maximo_tentativa = 0


print("Níveis de dificuldade")
print("\nSelecione o Nível\n(1) - Fácil\n(2) - Médio\n(3) - Díficil")

nivel = int(input(""))

if(nivel == 1):
        n_tentativas = 9
        maximo_tentativa = 9
        n_secreto = rd.randrange(1,31)
        entradajogo = int(input("Digita um número de 1 a 30! Não vale trapacear:"))
elif(nivel == 2):
        n_tentativas = 6
        maximo_tentativa = 6
        n_secreto = rd.randrange(1,61)
        entradajogo = int(input("Digita um número de 1 a 60! Não vale trapacear:"))
elif(nivel == 3):
        n_tentativas = 3
        maximo_tentativa = 3
        n_secreto = rd.randrange(1,91)
        entradajogo = int(input("Digita um número de 1 a 90! Não vale trapacear:"))


for n_tentativas in range(1,n_tentativas + 1):
    print(f"Tentativa {n_tentativas} de {maximo_tentativa}")
    entrada = entradajogo
    acertou = entrada == n_secreto
    entrada_maior = entrada > n_secreto
    entrada_menor = entrada < n_secreto

    if(entrada > 100 or entrada < 1):
        print("DIGITA UM NÚMERO DE VERDADE BESTAAAA!!")
        continue
    print(f"Você digitou isso aqui: {entrada}\n")

    #Verificação de acerto
    if(acertou):
        print("ACERTOOOOOO\n")
        break
    else:
        if(entrada_maior):
            print("Errrou! Mas o número é maior doque o secreto\n")
        if(entrada_menor):
            print("Errrou! Mas o número é menor doque o secreto\n")

print(f"Fim de Jogo, o número era {n_secreto}")














