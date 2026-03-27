def jogar_forca():
    print("---------------------------------")
    print("\n  Bem vindo ao Jogo da Forca!  \n")
    print("---------------------------------")

    lista = []

    palavra_secreta = "processador".upper()
    letras_acertadas = ["_","_","_","_","_","_","_","_","_","_","_"]
    perdeu = False
    acertou = False

    while not perdeu and not acertou:
        chute = input("Escreva uma letra: ")
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
                print(letras_acertadas)   
            index = index + 1
            
            
print()





if __name__ == "__main__":
    jogar_forca()