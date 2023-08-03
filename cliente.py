class Cliente:
    def __init__(self, user, senha, saldo_inicial):
        self.user = user
        self.senha = senha
        self.saldo = saldo_inicial

    def realizar_deposito(self, valor):
        self.saldo += valor

    def realizar_saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def obter_saldo(self):
        return self.saldo
