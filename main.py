class ContaCorrente:

    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self,valor):
        if self.saldo - valor < self.limite_conta():
            print('Você não tem saldo sufiiciente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor


#programa
conta_Maguila = ContaCorrente("Maguila","035.687.877-99")
conta_Maguila.consultar_saldo()

#depositando dinheiro
conta_Maguila.depositar(20000)
conta_Maguila.consultar_saldo()
#sacando dinheiro
conta_Maguila.sacar_dinheiro(20001)

print('Saldo Final')
conta_Maguila.consultar_saldo()
