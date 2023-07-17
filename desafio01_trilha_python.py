#Sistema bancário com operações: saque, depósito e extrato
menu = """
[1] deposito
[2] saque
[3] extrato
[0] sair
=> """

saldo = 0
limite = 500
qt_saque = 0
LIMITE_SAQUE = 3
extrato = ""

while True:
    opcao = input(menu)
    
    if opcao == "1": 
        deposito = float(input("Informe o valor de deposito: "))
        
        if deposito > 0:
            saldo += deposito
            print(f"Deposito realizado no valor de R$ {deposito:.2f}\n")
            extrato += f"Deposito realizado: R$ {deposito:.2f}\n"
        else:
            print("Não foi possivel realizar deposito, valor invalido!!")
   
    elif opcao == "2":
        saque = int(input("Informe o valor de saque: "))
        
        if saque > saldo:
            print("Você não possui saldo suficiente para essa operação")
            
        elif saque > limite:
            print("O valor do saque excedeu o limite")
            
        elif qt_saque >= LIMITE_SAQUE:
            print("Numero máximo de saques excedido!")
        
        elif saque > 0:
            saldo -= saque
            print(f"Saque realizado no valor R$ {saque:.2f}\n")
            extrato += f"Saque realizado: R$ {saque:.2f}\n"
            qt_saque +=1
        else:
            print("Não foi possivel realizar saque, valor inválido!!")
        
    elif opcao == "3":
        print("###### EXTRATO ######")
        print(f"SALDO: R$ {saldo:.2f}")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
    
    elif opcao == "0":
        break
    
    else:
        print("Opção invalida, por favor informe novamente a operação desejada!")