print("--Banco Sonegadinho--\n")

Saldo = "5.000,00 R$"
Sacar = "500 R$"
Desligar = False

while (Desligar != True):
    entrada = int(input("Digite 1 para ver o saldo, 2 para Sacar e 3 para Sair:"))

    if(entrada == 3):
        print("\nSe vai sair? puxaaaa :'(\n")
        Desligar = True
    else:
        if(entrada == 2):
            print(f"\nSe pode sacar até {Sacar}\n")
        if(entrada == 1):
            print(f"\nSeu Saldo é de {Saldo}\n")

    


