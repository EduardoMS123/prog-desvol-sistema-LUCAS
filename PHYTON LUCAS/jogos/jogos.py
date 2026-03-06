import jogoadvinhacao as jad
import forca as fc

print("---------------------")
print("\n  Escolha seu JOGO  \n")
print("---------------------")

print("(1)Jogo de Adivinhação\n(2)Jogo da Forca\n")

opcao_jogo = int(input("Escolha Seu Jogo: "))

if(opcao_jogo == 1):
    print("Escolhendo Advinhação...")
    jad.jogar_advinhacao()
elif(opcao_jogo == 2):
    print("Escolhendo Forca...")
    fc.jogar_forca()



