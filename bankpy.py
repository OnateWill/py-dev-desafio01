from bp_class import Bankpy

menu = """
---------- BankPy ----------

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)
    banco = Bankpy()

    if opcao == "d":
        valor = float(input("Qual o valor do depósito - R$:"))
        banco.deposito(valor)

    elif opcao == "s":
        valor = float(input("Qual o valor do saque - R$:"))
        banco.saque(valor)
    
    elif opcao == "e":
        banco.extrato()
    
    elif opcao == "q":
        break
    
    