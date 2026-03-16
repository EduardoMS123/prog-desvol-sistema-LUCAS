print('------------------------')
print('\n MERCADINHO DO SEU JOÃO \n')
print('------------------------')

minha_lista = ['(1)Morango','(2)Laranja','(3)Limão','(4)Sair']
iterador = iter(minha_lista) # Transforma em iterador
entrada = input("Você deseja comprar no Mercado do seu João? sim ou não?\n")

def compras():
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        fechar = False

        while (fechar != True):
            entrada2 = int(input(""))
            if entrada2 == 4:
                print("Aaaah, se vai sair?")
                fechar = True
            else: 
                if entrada2 == 1:
                    print("Você comprou um Morango, quer mais algo?")
                if entrada2 == 2:
                    print("Você comprou um Laranja, quer mais algo?")
                if entrada2 == 3:
                    print("Você comprou um Limão, quer mais algo?")

if(entrada == "sim"):
    print("Deus te abençoe, oque deseja?")
    compras()    
elif(entrada == "não"):
        print("Aaaaaah que pena :(")

    











