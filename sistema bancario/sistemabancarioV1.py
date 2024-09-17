menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[s] Sair

=> """

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
limite_quantidade_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_transacao = float(input("Informe o valor para depósito: "))

        if valor_transacao > 0:
            saldo += valor_transacao
            extrato += f"Depósito: R$ {valor_transacao:.2f}\n"

        else:
            print("O valor informado da trasação é invalido, favor informar novamente.")

    elif opcao == "2":
        valor_transacao = float(input("Informe o valor para saque: "))


        if valor_transacao > saldo:
            print("Não foi possivel realizar o saque, pois não há saldo suficiente.")

        elif valor_transacao > limite_valor_saque:
            print("Não foi possivel realizar o saque, pois o valor está acima do limite permitido.")

        elif numero_saques >= limite_quantidade_saques:
            print("Saque indiponivel. Você excedeu o seu limite diario de saques.")

        elif valor_transacao > 0:
            saldo -= valor_transacao
            extrato += f"Saque: R$ -{valor_transacao:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado da trasação é invalido, favor informar novamente.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "s":
        break

    else:
        print("Opção informada é inválido. Por favor, escolha novamente!")