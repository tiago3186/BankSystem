from banco import Banco

def main():
    banco = Banco()
    print("Bem-vindo ao Banco Simples!")

    while True:
        print("\nOpções:")
        print("1 - Criar conta")
        print("2 - Login")
        print("3 - Sair")
        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            user = input("Digite o usuário desejado: ")
            senha = input("Digite a senha desejada: ")
            saldo_inicial = float(input("Digite o saldo inicial: "))
            if banco.criar_conta(user, senha, saldo_inicial):
                print("Conta criada com sucesso!")
            else:
                print("Usuário já existe. Escolha outro usuário.")
        elif opcao == 2:
            user = input("Digite o usuário: ")
            senha = input("Digite a senha: ")
            cliente = banco.login(user, senha)
            if cliente:
                print("Login realizado com sucesso!")
                while True:
                    print("\nOpções:")
                    print("1 - Depósito")
                    print("2 - Saque")
                    print("3 - Extrato")
                    print("4 - Sair")
                    opcao = int(input("Digite o número da opção desejada: "))

                    if opcao == 1:
                        valor = float(input("Digite o valor do depósito: "))
                        cliente.realizar_deposito(valor)
                        print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${cliente.obter_saldo():.2f}")
                    elif opcao == 2:
                        valor = float(input("Digite o valor do saque: "))
                        if cliente.realizar_saque(valor):
                            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${cliente.obter_saldo():.2f}")
                        else:
                            print("Saldo insuficiente.")
                    elif opcao == 3:
                        print(f"Extrato do cliente {user}:")
                        print(f"Saldo atual: R${cliente.obter_saldo():.2f}")
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
