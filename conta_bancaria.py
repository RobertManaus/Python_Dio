menu = '''
            ******* MENU *******
            ====================
            [ D ] - DEPOSITAR
            [ S ] - SACAR
            [ E ] - EXTRATO
            [ Q ] - SAIR
            ====================
'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    op = input(menu)
    opcao = (op.upper())

    if opcao == "D":
        valor = float(input("VALOR DO DEPOSITO..: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito..: R$ {valor:.2f}"
        else:
            print('''
                    FALHA NA OPERACAO!
                    VALOR INVALIDO!
                ''')
    elif opcao == "S":
        valor = float(input("VALOR DO SAQUE..: R$ "))
        if valor > saldo:
            print('''
                    OPERACAO FALHOU!
                    SALDO INSUFICIENTE!            
            ''')
        
        elif valor > limite:
            print('''
                    OPERACAO FALHOU!
                    VALOR DO SAQUE EXCEDEU O LIMITE!
            ''')
        
        elif valor > 0 and numero_saque <= 3:
            saldo -= valor
            extrato += f"Saque..: R$ {valor:.2f}\n"
            numero_saque += 1
            
        else:
            print('''
                    OPERACAO FALHOU!   
                    VALOR INFORMADO INVALIDO!
            ''')

    elif opcao == "E":
        print("\n===========  EXTRATO  ===========\n")
        print("NÃO FORAM REALIZADAS MOVIMENTACOES." if not extrato else extrato)
        print(f"\nSALDO..: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "Q":
        print("SAINDO DO SISTEMA...")
        break

    else:
        print('''
                OPERACAO FALHOU!
                SELECIONE OPERACAO VALIDA.
        ''')