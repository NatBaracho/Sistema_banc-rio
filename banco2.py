def exibir_menu():
    menu = """
========= MENU ============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
===========================

=> """
    return input(menu).lower()


def depositar(saldo, extrato):
    try: # O bloco try/except permite tentar executar um trecho de código e, se der erro, tratar esse erro de forma controlada, sem quebrar o programa.

        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Valor inválido. Tente novamente.")

    except ValueError:
        print("Entrada inválida! Digite um número.")
        
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    try:
        valor = float(input("Digite o valor que deseja sacar: "))

        if valor <= 0:
            print("Valor inválido. Tente novamente.")

        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif valor > limite:
            print(f"Operação falhou! O limite por saque é R$ {limite:.2f}.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques atingido.")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    except ValueError:
        print("Entrada inválida! Digite um número.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Nenhuma movimentação registrada." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================\n")


def main():
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

main()