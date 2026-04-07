def jogar_forca():
    print("---------------------------------")
    print("\n  Bem vindo ao Jogo da Forca!  \n")
    print("---------------------------------")

    lista = []

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in palavras:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = "processador".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    #for letra in palavra_secreta
        #letras_acertadas.append("_")

    perdeu = False
    acertou = False
    erros = 0

    while not perdeu and not acertou:
        chute = input("Escreva uma letra: ")
        chute = chute.strip().upper()

        index = 0
        if chute in palavra_secreta:

            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                    print(letras_acertadas)
                index += 1
        else:
            erros += 1
            
        perdeu = erros == 6
        acertou = "_" not in letras_acertadas

        

            
    





if __name__ == "__main__":
    jogar_forca()