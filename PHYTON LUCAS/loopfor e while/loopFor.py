print("-----------------------")
print("O NÚMERO É PAR OU IMPAR???")
print("-----------------------")

rodada = 1

for rodada in range(2):
    entrada = int(input("Digita um número:"))

    if entrada % 2 == 0:
        print(f"O número {entrada} é um número par")
        break
    else:
        print(f"Eita!! o número {entrada} é um número impar!")
        break

