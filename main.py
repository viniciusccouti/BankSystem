from ContasBancos import ContaCorrente, CartaoCredito

#programa
conta_Maguila = ContaCorrente("Maguila","035.687.877-99", 1234, 23456)

cartao_Maguila = CartaoCredito('Maguila', conta_Maguila)

conta_Maguila.nome = "Maguila o Gorila"
print(conta_Maguila.nome)

cartao_Maguila.senha = '2345'
print(cartao_Maguila.senha)

print(conta_Maguila.__dict__)