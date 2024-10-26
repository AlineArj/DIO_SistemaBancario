def Menu():
    pass

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
    
    if saques_realizados > MAX_SAQUES:
        return print(f"\n\n/!\ AÇÃO INDISPONÍVEL /!\ - Limite de saques excedido.\n\n")
    
    else:
            print(f"\n\n### SAQUE ###")
            valor_saque = float(input("Valor desejado: R$ "))
            
            if valor_saque <= 0:
                return print("\n\n /!\ ERRO /!\ - Valor invalido para saque.\n\n")
            elif valor_saque > VALOR_MAX_SAQUES:
                return print("\n\nSAQUE NEGADO: Valor do saque acima do permitido.\n\n")
            elif valor_saque > saldo:
                print("\n\nSAQUE NEGADO: Saldo insuficiente para completar a operação.\n\n")
                return 'falha', valor_saque, saldo
            else:
                saldo -= valor_saque
                print(f"\nSaque realizado com sucesso!\n\n")
                return 'sucesso', (valor_saque * -1), saldo 
            
            
            


MAX_SAQUES = 3
VALOR_MAX_SAQUES = 300

saldo_em_conta = 1000
operacao = [('sucesso', 0, saldo_em_conta)] # Registra as caracteristicas da operação
saques_realizados = 0


while True:
    # apoio = Deposito(saldo_em_conta)
    
    # if apoio == None: continue
    # else:
    #     operacao.append(apoio)
    #     saldo_em_conta = operacao[-1][-1]
    #     print(saldo_em_conta)
    #     print(operacao)
    
    # apoio = Saque(saldo_em_conta,saques_realizados)

    # if apoio == None: continue
    # else:
    #     operacao.append(apoio)
    #     saldo_em_conta = operacao[-1][-1]
    #     if operacao[-1][0] == 'sucesso': saques_realizados += 1 
        
    # print(saldo_em_conta)
    # print(operacao)
        pass