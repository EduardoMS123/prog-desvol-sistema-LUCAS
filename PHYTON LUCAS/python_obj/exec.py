from conta import Conta

conta1 = Conta(535, "Ricardo", 55.0, 1000.0)
conta2 = Conta(536, "Larissa", 105.0, 1000.0)

conta1.extrato()
conta1.depositar(2000)
conta1.extrato()
print(conta2.codigo_banco())
codigos = Conta.codigos_bancos()
print(codigos['Caixa'])




