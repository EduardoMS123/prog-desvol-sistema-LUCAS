
print('------------------------')
print('\n MERCADINHO DO SEU JOÃO \n')
print('------------------------')

minha_lista = ['(1)Morango','(2)Laranja','(3)Limão']
iterador = iter(minha_lista) # Transforma em iterador
entrada = input("Você deseja comprar no Mercado do seu João? sim ou não?\n")

if(entrada == "sim"):
    print("Deus te abençoe, oque deseja?")
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    entrada2 = input("")
    if(entrada2 == 'Morango'):
        print('Morango comprado!')
    if(entrada2 == 'Laranja'):
        print('Laranja comprada!')
    if entrada2 == 'Limão':
        print('Limão comprado')
elif(entrada == "não"):
    print("Aaaaaah que pena :(")











