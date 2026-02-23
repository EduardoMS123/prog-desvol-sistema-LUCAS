import random as rd

print("-----------------------------")
print("\nBem vindo ao jogo de ADIVINHA\n")
print("-----------------------------")

#definir a variavel
n_secreto = rd.randrange(1,51)
n_tentativas = 5
maximo_tentativa = 5

for n_tentativas in range(1,n_tentativas + 1):
    print(f"Você está na tentativa: {n_tentativas}/{maximo_tentativa}")
    entrada = int(input("Digita um número ai mano! De 1 a 50 ein, não vale trapacear!:"))
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














