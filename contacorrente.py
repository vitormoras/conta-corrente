class ContaCorrente():
    def __init__(self, num_conta, nome_corrent, saldo = 0):
        self.num_conta = num_conta
        self.nome_corrent = nome_corrent
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nome_corrent = novo_nome

    def xSaldo(self):
        return f'Seu saldo atual é de R$ {self.saldo}'
    
    def deposito(self, novo_saldo):
        self.saldo += novo_saldo

    def saque(self, valor_saque):
        self.saldo -= valor_saque

    def infoConta(self):
        return f'O número da conta é {self.num_conta}\n O nome do títular da conta é {self.nome_corrent}\n e o saldo atual é de R$ {self.saldo}'

conta = ContaCorrente('696969', 'Noninho')
print(conta.xSaldo())
conta.deposito(1500)
print(conta.xSaldo())
print(conta.infoConta())

conta.alterarNome('Botieli')
conta.saque(750)
conta.saque(344)

print(conta.infoConta())