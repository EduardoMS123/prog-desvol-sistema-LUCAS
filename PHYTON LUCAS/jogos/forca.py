def jogar_forca():
    print("---------------------------------")
    print("\n  Bem vindo ao Jogo da Forca!  \n")
    print("---------------------------------")

    palavra_secreta = "processador"
    perdeu = False
    acertou = False

    while not perdeu and not acertou:
        chute = input("Escreva uma letra: ")
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print(f"A letra {chute} está na posição {index}")
            index = index + 1


















if __name__ == "__main__":
    jogar_forca()