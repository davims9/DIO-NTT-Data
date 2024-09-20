from datetime import datetime

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
limite_saques_dia = 10
data_anterior = "" 

while True:

    opcao = input(menu)
    data_hoje = (datetime.now()).strftime("%d/%m/%Y")

    if data_hoje != data_anterior:
        numero_saques = 0
        data_anterior = data_hoje

    if opcao == "1":
        valor_transacao = float(input("Informe o valor para depósito: "))

        if valor_transacao > 0:
            saldo += valor_transacao
            extrato += f"Depósito: R$ {valor_transacao:.2f} {(datetime.now()).strftime('%d/%m/%Y %H:%M:%S')}\n"

        else:
            print("O valor informado da transação é inválido, favor informar novamente.")

    elif opcao == "2":
        valor_transacao = float(input("Informe o valor para saque: "))

        if valor_transacao > saldo:
            print("Não foi possível realizar o saque, pois não há saldo suficiente.")

        elif valor_transacao > limite_valor_saque:
            print("Não foi possível realizar o saque, pois o valor está acima do limite permitido.")

        elif numero_saques >= limite_saques_dia:
            print("Saque indisponível. Você excedeu o seu limite diário de saques.")

        elif valor_transacao > 0:
            saldo -= valor_transacao
            extrato += f"Saque: R$ -{valor_transacao:.2f} {(datetime.now()).strftime('%d/%m/%Y %H:%M:%S')}\n"
            numero_saques += 1

        else:
            print("O valor informado da transação é inválido, favor informar novamente.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "s":
        break

    else:
        print("Opção informada é inválida. Por favor, escolha novamente!")
