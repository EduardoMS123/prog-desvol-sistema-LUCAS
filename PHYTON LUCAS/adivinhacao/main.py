print("-----------------------------")
print("\nBem vindo ao jogo de ADIVINHA\n")
print("-----------------------------")

n_secreto = 4123
entrada = int(input("Digita um número ai mano! ->"))
acertou = entrada == n_secreto
entrada_maior = entrada > n_secreto
entrada_menor = entrada < n_secreto

print(f"Você digitou isso aqui -> {entrada}\n")

#Verificação de acerto
if(acertou):
    print("ACERTOOOOOO\n") 
else:
    if(entrada_maior):
       print("Errrou! Mas o número é maior doque o secreto\n")
    if(entrada_menor):
       print("Errrou! Mas o número é menor doque o secreto\n")

print("Cabou o games, valeuzão por jogar")















