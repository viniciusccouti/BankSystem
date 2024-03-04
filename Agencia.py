from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O valor de Caixa está ok. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa')


    def adicionar_cliente(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))

class AgenciaVirtual(Agencia):

    def __init__(self,site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
    def sacar_paypal(self):
        self.caixa += valor
        self.caixa_paypal -= valor



class AgenciaComum(Agencia):

    def __init__(self,telefone, cnpj):
        super().__init__(telefone,cnpj,numero=(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=(1001, 9999))
        self.caixa = 10000000


agencia1 = Agencia(22222233, 147899888, 4567)

agencia_virtual = AgenciaVirtual('www.gorila.com.br', 221212, 21113)
agencia_virtual.verificar_caixa()

agencia_comum = AgenciaComum(2222222, 2313131)

agencia_premium = AgenciaPremium(2222131,23213123)
agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)


