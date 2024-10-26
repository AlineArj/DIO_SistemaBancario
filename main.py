def Menu():
    
    print(f"- MENU -".center(50))
    print(f"[ 1 ] - Depósito".center(50))
    print(f"[ 2 ] - Saque".rjust(30))
    print(f"[ 3 ] - Extrato".center(50))
    print(f"[ 0 ] - SAIR".rjust(29))
    
    return int(input("\nEscolha uma opção: "))


def Deposito(saldo):
    
    print(f"\n\n### DEPOSITO ###")
    valor_deposito = float(input("Valor desejado: R$ "))
    
    if valor_deposito < 1:
        print("\n\n /!\ ERRO /!\ - Valor invalido para deposito.\n\n") 
        return 
    else:
        saldo += valor_deposito
        print(f"\nDeposito realizado com sucesso!\n\n")
        return 'sucesso', valor_deposito, saldo


def Saque(saldo, saques_realizados):
    
    if saques_realizados >= MAX_SAQUES:
        return print(f"\n\n/!\ AÇÃO INDISPONÍVEL /!\ - Limite de saques excedido para esta conta.\n\n")
    
    else:
            print(f"\n\n### SAQUE ###")
            valor_saque = float(input("Valor desejado: R$ "))
            
            if valor_saque <= 0:
                return print("\n\n /!\ ERRO /!\ - Valor invalido para saque.\n\n")
            elif valor_saque > VALOR_MAX_SAQUES:
                return print("\n\nSAQUE NEGADO: Valor do saque acima do permitido.\n\n")
            elif valor_saque > saldo:
                print("\n\nSAQUE NEGADO: Saldo insuficiente para completar a operação.\n\n")
                return 'falha', (valor_saque * -1), saldo
            else:
                saldo -= valor_saque
                print(f"\nSaque realizado com sucesso!\n\n")
                return 'sucesso', (valor_saque * -1), saldo 


def Extrato(hist_operacao):
    contador = len(hist_operacao)
    
    print(f"\n\n### EXTRATO ###")
    print(f"SALDO INICIAL: R$ {hist_operacao[0][-1]:.2f}\n")
    
    if contador == 1: return print("Não houve operações.\n\n")
    else:
        for operação in range(contador):
            if operação == 0: pass
            
            elif hist_operacao[operação][0] == 'sucesso':
                if hist_operacao[operação][1] < 0:
                    print(f"- Saque #{operação}: -R$ {abs(hist_operacao[operação][1]):.2f}")
                else: print(f"- Deposito #{operação}: R$ {hist_operacao[operação][1]:.2f}")
            else:
                print(f"- Saque Negado #{operação}: -R$ {abs(hist_operacao[operação][1]):.2f}")
        
        print(f"\nSALDO FINAL: R$ {hist_operacao[-1][-1]:.2f}\n\n")
                        
            
MAX_SAQUES = 3
VALOR_MAX_SAQUES = 300

saldo_em_conta = 0
hist_operacao = [('sucesso', 0, saldo_em_conta)] # Registra as caracteristicas da operação
saques_realizados = 0

# Cabeçalho
print('\n')
print(f"{'_' * 50}")
print(f"BANCO ALINE".center(50))
print(f"{'—' * 50}")
print('\n')

while True:
    opcao = Menu()
    
    if opcao == 1:
        apoio = Deposito(saldo_em_conta)
        
        if apoio == None: continue
        else:
            hist_operacao.append(apoio)
            saldo_em_conta = hist_operacao[-1][-1]
    
    elif opcao == 2:
        apoio = Saque(saldo_em_conta,saques_realizados)

        if apoio == None: continue
        else:
            hist_operacao.append(apoio)
            saldo_em_conta = hist_operacao[-1][-1]
            print(hist_operacao[-1][0])
            if hist_operacao[-1][0] == 'sucesso': saques_realizados += 1 
        
    elif opcao == 3: Extrato(hist_operacao)
        
    elif opcao == 0:
        print('\n\n')
        print(f"{'_' * 50}")
        print(f"Banco Aline agradece a sua preferencia.".center(50))
        print(f"VOLTE SEMPRE!".center(50))
        print(f"{'_' * 50}")
        break
    
    else: print(f"\n\n/!\ ERRO /!\ - A opção selecionada é inválida, tente novamente!\n\n")