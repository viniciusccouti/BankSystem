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

    pass

class AgenciaComum(Agencia):

    pass

class AgenciaPremium(Agencia):

    pass


agencia1 = Agencia(22222233, 147899888, 4567)
agencia1.caixa = 1000000
agencia_virtual = AgenciaVirtual(2222,4444432,7897)

agencia_virtual.caixa = 15000
agencia_virtual.verificar_caixa()

agencia_premium = AgenciaPremium(3333,213,2222)
agencia_premium.caixa = 100000
agencia_premium.verificar_caixa()

