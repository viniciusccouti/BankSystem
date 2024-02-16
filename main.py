from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

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

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor,Saldo,Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))



#programa
conta_Maguila = ContaCorrente("Maguila","035.687.877-99", 1234, 23456)
conta_Maguila.consultar_saldo()

#depositando dinheiro
conta_Maguila.depositar(8000)
conta_Maguila.consultar_saldo()

print('Saldo Final')
conta_Maguila.consultar_saldo()
conta_Maguila.consultar_limite_chequeespecial()

print('-'*20)

print(conta_Maguila.consultar_historico_transacoes())
print('-'*20)

conta_Chokito = ContaCorrente('Chokito','1234232','3474','22345')
conta_Maguila.transferir(1000,conta_Chokito)

conta_Maguila.consultar_saldo()
conta_Chokito.consultar_saldo()

conta_Maguila.consultar_historico_transacoes()
conta_Chokito.consultar_historico_transacoes()