from cliente import Cliente

class Banco:
    def __init__(self):
        self.clientes = {}

    def criar_conta(self, user, senha, saldo_inicial):
        if user in self.clientes:
            return False
        cliente = Cliente(user, senha, saldo_inicial)
        self.clientes[user] = cliente
        return True

    def login(self, user, senha):
        if user in self.clientes and self.clientes[user].senha == senha:
            return self.clientes[user]
        return None
