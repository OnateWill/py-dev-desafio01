class Bankpy:

    def __init__(self):
        self.__saldo = 0
        self.__limite = 500
        self.__extrato = ''
        self.__nsaques = 0
        self.__LIMITE_SAQUES = 3

    def deposito(self, valor):
        valor = valor
        extrato = self.__extrato
        
        if valor > 0:
            self.__saldo += valor
            extrato += f"Depósito: R$: {valor:.2f}\n"
            print(f"Depósito realizado com sucesso")
        
        else:
            print("Operação falhou! Valor inválido.")
    
    def saque(self, valor):
        valor = valor
        saldo = self.__saldo
        numero_de_saques = self.__nsaques
        extrato = self.__extrato
        limite_saques = self.__LIMITE_SAQUES

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > saldo
        excedeu_saques = numero_de_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor excedeu o limite de saque.")
        
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")
        
        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$: {valor:.2f}\n"
            numero_de_saques += 1
            print("Saque Realizado.")
        
        else:
            print("Operação Falhou! O valor informado é inválido")


    def extrato(self):
        saldo = self.__saldo
        extrato = self.__extrato

        print(f"\n{'='*10} EXTRATO {'='*10}")
        print(f"Não foram realizadas movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$:{saldo:.2f}")
        print(f"{'='*10} EXTRATO {'='*10}")
    


"""


"""