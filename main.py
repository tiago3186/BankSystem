# Dados dos clientes (usuário, senha, saldo)
clientes = {}

# Função para realizar o login do cliente
def login():
    user = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if user in clientes and clientes[user]["senha"] == senha:
        return user
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return None

# Função para criar uma nova conta
def criar_conta():
    user = input("Digite o usuário desejado: ")
    while user in clientes:
        print("Usuário já existe. Escolha outro usuário.")
        user = input("Digite o usuário desejado: ")

    senha = input("Digite a senha desejada: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    clientes[user] = {"senha": senha, "saldo": saldo_inicial}

    print("Conta criada com sucesso!")

    return user

# Função para realizar um depósito
def deposito(user):
    valor = float(input("Digite o valor do depósito: "))
    clientes[user]["saldo"] += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${clientes[user]['saldo']:.2f}")

# Função para realizar um saque
def saque(user):
    valor = float(input("Digite o valor do saque: "))
    if valor <= clientes[user]["saldo"]:
        clientes[user]["saldo"] -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${clientes[user]['saldo']:.2f}")
    else:
        print("Saldo insuficiente.")

# Função para exibir o extrato
def extrato(user):
    print(f"Extrato do cliente {user}:")
    print(f"Saldo atual: R${clientes[user]['saldo']:.2f}")

# Função principal
def main():
    print("Bem-vindo ao Banco Simples!")

    while True:
        print("\nOpções:")
        print("1 - Criar conta")
        print("2 - Login")
        print("3 - Sair")
        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            user = login()
            if user:
                print("Login realizado com sucesso!")
                while True:
                    print("\nOpções:")
                    print("1 - Depósito")
                    print("2 - Saque")
                    print("3 - Extrato")
                    print("4 - Sair")
                    opcao = int(input("Digite o número da opção desejada: "))

                    if opcao == 1:
                        deposito(user)
                    elif opcao == 2:
                        saque(user)
                    elif opcao == 3:
                        extrato(user)
                    elif opcao == 4:
                        print("Sessão encerrada.")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
        elif opcao == 3:
            print("Obrigado por usar o Banco Simples. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
