from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self,nome,cpf, agencia,num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo,ContaCorrente._data_hora()))

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self,valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo sufiiciente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de chque especial é de {:,.2f}'.format(self._limite_conta()))


#programa
conta_Maguila = ContaCorrente("Maguila","035.687.877-99", 1234, 23456)
conta_Maguila.consultar_saldo()

#depositando dinheiro
conta_Maguila.depositar(20000)
conta_Maguila.consultar_saldo()
#sacando dinheiro
conta_Maguila.sacar_dinheiro(20900)

print('Saldo Final')
conta_Maguila.consultar_saldo()
conta_Maguila.consultar_limite_chequeespecial()

print('-'*20)

print(conta_Maguila.transacoes)
