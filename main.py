class ContaCorrente:

    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar_dinheiro(self,valor):
        self.saldo -= valor


#programa
conta_Maguila = ContaCorrente("Maguila","035.687.877-99")
conta_Maguila.consultar_saldo()

#depositando dinheiro
conta_Maguila.depositar(8000)
conta_Maguila.consultar_saldo()
#sacando dinheiro
conta_Maguila.sacar_dinheiro(7600)
conta_Maguila.consultar_saldo()
