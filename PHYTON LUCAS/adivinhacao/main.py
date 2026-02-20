print("-----------------------------")
print("\nBem vindo ao jogo de ADIVINHA\n")
print("-----------------------------")

#definir a variavel
n_secreto = 4123
n_tentativas = 5
maximo_tentativa = 5

for n_tentativas in range(1,n_tentativas + 1):
    print(f"Você está na tentativa: {n_tentativas}/{maximo_tentativa}")
    entrada = int(input("Digita um número ai mano!:"))
    acertou = entrada == n_secreto
    entrada_maior = entrada > n_secreto
    entrada_menor = entrada < n_secreto

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
    

print("Cabou o games, valeuzão por jogar")














