import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1] Nova usuario
    [2] Novo conta
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Listar contas
    [7] Remover conta
    [0] Sair
    => """
    return input(textwrap.dedent(menu))

def novo_usuario(usuarios):
    cpf = input("Informe o CPF: (somente números) ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já está cadastrado no sistema!!!")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf":cpf, "endereco": endereco})

    print("### Usuário cadastrado com sucesso! ###")

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: (somente números) ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("### Conta criada com sucesso! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("### Falha ao criar conta, usuário não encontrado!! ###")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha).strip())

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def remover_conta(numero_conta, contas):
    for i, conta in enumerate(contas):
        if conta["numero_conta"] == numero_conta:
            del contas[i]
            print(f"Conta {numero_conta} removida com sucesso!")
            return

    print(f"Não foi encontrada uma conta com o número {numero_conta}.")


def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        print(f"Depósito realizado no valor de R$ {deposito:.2f}\n")
        extrato += f"Depósito realizado: R$ {deposito:.2f}\n"
    else:
        print("Não foi possível realizar depósito, valor inválido!!")
       
    return saldo, extrato
    
def sacar(*, saldo, saque, extrato, limite, qt_saque, limite_saque):
    if saque > saldo:
        print("Você não possui saldo suficiente para essa operação")
    elif saque > limite:
        print("O valor do saque excedeu o limite")
    elif qt_saque >= limite_saque:
        print("Número máximo de saques excedido!")
    elif saque > 0:
        saldo -= saque
        print(f"Saque realizado no valor de R$ {saque:.2f}\n")
        extrato += f"Saque realizado: R$ {saque:.2f}\n"
        qt_saque += 1
    else:
        print("Não foi possível realizar saque, valor inválido!!")
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("###### EXTRATO ######")
    print(f"SALDO: R$ {saldo:.2f}")
    print("Não foram realizadas movimentações!" if not extrato else extrato)
    
    return saldo, extrato

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    qt_saque = 0
    extrato = ""
    contas = []
    usuarios = []

    while True:
        opcao = menu()
    
        if opcao == "1":
            novo_usuario(usuarios)
                 
        elif opcao == "2": 
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
     
        elif opcao == "3": 
            deposito = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == "4":
            saque = int(input("Informe o valor de saque: "))
            saldo, extrato = sacar(saldo=saldo, saque=saque, extrato=extrato, limite=limite, qt_saque=qt_saque, limite_saque=LIMITE_SAQUE)
                  
        elif opcao == "5":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "6": 
            listar_contas(contas)
        
        elif opcao == "7":
            numero_conta = input("Informe o número da conta a ser removida: ")
            remover_conta(numero_conta, contas)
            
        elif opcao == "0":
            break
        
        else:
            print("Opção inválida, por favor informe novamente a operação desejada!")

main()
