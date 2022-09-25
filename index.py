# Imports
import os

# Inicializando variáveis
nome_do_cliente = ''
saldo_atual = 0
saldo_inicial = 0
qtd_dep_realizados = 0
valor_total_dep_realizados = 0
qtd_saques_realizados = 0
valor_total_saques_realizados = 0
valor_total_juros_recebidos = 0
saldo_min_conta = 0
saldo_max_conta = 0


# Menu com as opções de escolha
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print('\n..:: Sua conta ::..\n')
    print('[1] Depósito')
    print('[2] Saque')
    print('[3] Aplicar Juros')
    print('[4] Simular Empréstimo')
    print('[5] Extrato')
    print('[9] Sair\n')

    # Solicita que usuário informe uma opção e guarda em variável
    selecionado = input('Escolha uma opção: ')

    # Retorna opção selecionada
    return selecionado


# Função que abre conta
def abrir_conta():
    print('\n..:: Abertura de conta ::..\n')
    # Salva o nome do cliente em uma variável global
    global nome_do_cliente
    nome_do_cliente = input(print("Digite o nome do cliente: "))

    # Salva o saldo do cliente em uma variável global
    global saldo_atual
    saldo_atual = float(input(print("Digite o saldo inicial da conta: ")))

    # Define o saldo inicial com o valor digitado e salva em global
    global saldo_inicial
    saldo_inicial = saldo_atual

    # Executa função que define saldo máximo e mínimo
    saldos_min_max_inicial()


# Função da opção 1 do menu
def option_1():
    print('\n..:: Depósito ::..\n')

    # Solicita cliente informe o valor para depósito
    valor_deposito = float(input(print("Digite o valor a ser depositado: ")))

    # Verifica se foi digitado um número maior que zero
    if (type(valor_deposito) == int or type(valor_deposito) == float) and valor_deposito > 0:

        # Chama a variável global saldo atual
        global saldo_atual

        # Mostra saldo atual antes do depósito
        print("Saldo anterior: ", saldo_atual)

        # Soma valor depositado na variável saldo atual
        saldo_atual += valor_deposito

        # Mostra saldo atual após depósito
        print("Saldo atual: ", saldo_atual)

        # Contabiliza o depósito para a variável total depósitos
        global qtd_dep_realizados
        qtd_dep_realizados += 1

        # Contabiliza o valor depósito para a variável de valor total depósitos
        global valor_total_dep_realizados
        valor_total_dep_realizados += valor_deposito

        # Executa função que define saldo máximo
        saldo_maximo()
    else:
        # Mostra mensagem de erro caso valor informado seja inválido
        print("Valor inválido!", valor_deposito)


# Função da opção 2 do menu
def option_2():
    print('\n..:: Saque ::.. 2\n')

    # Solicita usuário informe o valor para depósito
    valor_saque = float(input(print("Digite o valor a ser sacado: ")))

    # Verifica se foi digitado um número válido
    if (type(valor_saque) == int or type(valor_saque) == float) and valor_saque > 0:

        # Chama a variável global saldo atual
        global saldo_atual

        # Verifica se saldo atual é maior que saque
        if saldo_atual >= valor_saque:

            # Mostra saldo antes do saque
            print("Saldo anterior: ", saldo_atual)

            # Chama variável global valor total de saques realizados
            global valor_total_saques_realizados

            # Soma saque no valor total de saques realizados
            valor_total_saques_realizados += valor_saque

            # Contabiliza o saque para a variável de total saques
            global qtd_saques_realizados
            qtd_saques_realizados += 1

            # Subtrai saque do saldo atual
            saldo_atual = saldo_atual - valor_saque

            # Executa função que define saldo mínimo
            saldo_minimo()

            # Mostra saldo atual após saque
            print("Saldo atual: ", saldo_atual)

            # Mostra valor sacado
            print("Valor sacado: ", valor_saque)

            # Retorna notas liberadas
            notas(valor_saque)

        else:
            # Mostra erro caso valor saque maior que saldo atual
            print("Saldo Insuficiente", saldo_atual)
    else:
        # Mostra mensagem de erro caso valor informado seja inválido
        print("Valor inválido!", valor_saque)


# Função da opção 3 do menu
def option_3():
    print('\n..:: Aplicar Juros ::..\n')

    # Solicita usuário informe o valor da taxa de juros
    taxa_juros = float(input(print("Digite o valor da taxa de juros: ")))

    # Verifica se foi digitado um número válido
    if (type(taxa_juros) == int or type(taxa_juros) == float) and taxa_juros > 0:

        # Chama global saldo atual
        global saldo_atual

        # Mostra saldo atual antes do saque
        print("Saldo anterior: ", saldo_atual)

        # Calcula saldo com taxa de juros aplicada
        saldo = (saldo_atual * (1 + taxa_juros / 100))

        # Calcula o valor total de juros
        total_juros = saldo - saldo_atual

        # Soma valor total de juros global
        global valor_total_juros_recebidos
        valor_total_juros_recebidos += total_juros

        # Atualiza saldo atual
        saldo_atual = saldo

        # Chama funçãod e saldo máximo
        saldo_maximo()

        # Mostra saldo atual antes do saque
        print("Juros aplicado: ", taxa_juros)
        # Mostra saldo atual antes do saque
        print("Saldo atual: ", saldo_atual)

    else:
        # Mensagem de erro caso valor digitado seja inválido
        print("Valor inválido!")


# Função da opção 4 do menu
def option_4():
    print('\nSimular Empréstimo: 4\n')

    # Solicita valores ao usuário
    valor_emprestimo = float(input(print("Digite o valor do empréstimo: ")))
    taxa_juros = float(input(print("Digite o valor da taxa de juros: ")))
    parcelas = int(input(print("Digite o total de parcelas para pagamento: ")))

    # Verifica se valor empréstimo digitado é valido
    if (type(valor_emprestimo) == int or type(valor_emprestimo) == float) and valor_emprestimo > 0:
        # Verifica se taxa de juros digitado é valido
        if (type(taxa_juros) == int or type(taxa_juros) == float) and taxa_juros > 0:
            # Verifica se o valor de parcelas digitado é valido
            if type(parcelas) == int and parcelas > 0:
                # Mostra saldo atual antes do saque
                print("Juros aplicado: ", taxa_juros)

                # Calcula montante
                montante = valor_emprestimo * ((1 + taxa_juros / 100) ** parcelas)

                # Calcula valor da parcela
                valor_parcela = montante / parcelas

                # Calcula o valor total de juros
                juros = montante - valor_emprestimo

                # Mostra as informações na tela
                print("O valor da parcela foi de: " + str("R$ %.2f" % valor_parcela))
                print("O montante final foi de: " + str("R$ %.2f" % montante))
                print("Os juros foram de: " + str("R$ %.2f" % juros))
            else:
                # Mensagem de erro caso parcela digitada seja inválida
                print("Parcela inválida")
        else:
            # Mensagem de erro caso juros digitados seja inválida
            print("Juros inválido!")
    else:
        # Mensagem de erro caso valor digitado seja inválida
        print("Valor inválido")


# Função da opção 5 do menu
def option_5():
    print('\nExtrato: 5\n')

    # Mostra nome do cliente
    global nome_do_cliente
    print("Nome do Cliente: ", nome_do_cliente)

    # Mostra saldo inicial
    global saldo_inicial
    print("Seu saldo inicial: ", saldo_inicial)

    # Mostra o saldo atual
    global saldo_atual
    print("Seu saldo atual: ", saldo_atual)

    # Mostra qtd de dep realizados
    global qtd_dep_realizados
    print("Depósitos realizados: ", qtd_dep_realizados)

    # Mostra valor total de dep realizados
    global valor_total_dep_realizados
    print("Valor total depósitos realizados: ", valor_total_dep_realizados)

    # Mostra qtd de saques realizados
    global qtd_saques_realizados
    print("Saques realizados: ", qtd_saques_realizados)

    # Mostra valor total de saques realizados
    global valor_total_saques_realizados
    print("Valor total saques realizados: ", valor_total_saques_realizados)

    # Mostra valor total de juros recebidos
    global valor_total_juros_recebidos
    print("Valor total juros recebidos: ", valor_total_juros_recebidos)

    # Mostra o saldo mínimo da conta
    global saldo_min_conta
    print("Saldo mínimo da conta: ", saldo_min_conta)

    # Mostra o saldo máximo da conta
    global saldo_max_conta
    print("Saldo máximo da conta: ", saldo_max_conta)


# Função que define saldo mínimo da conta
def saldo_minimo():
    # Chama variáveis globais
    global saldo_min_conta
    global saldo_atual

    # Condicional que define se saldo atual é o saldo mínimo da conta
    if saldo_atual < saldo_min_conta:
        saldo_min_conta = saldo_atual


# Função que define saldo máximo da conta
def saldo_maximo():
    # Chama variáveis globais
    global saldo_max_conta
    global saldo_atual

    # Condicional que define se saldo atual é o saldo máximo da conta
    if saldo_atual > saldo_max_conta:
        saldo_max_conta = saldo_atual


# Função que define saldos min e max com o valor do saldo atual
def saldos_min_max_inicial():
    global saldo_min_conta
    global saldo_max_conta
    global saldo_atual
    saldo_min_conta = saldo_atual
    saldo_max_conta = saldo_atual


# Função que mostra notas que serão liberadas, passando o valor do saque como parâmetro
def notas(valor_saque):
    # Define quantas notas de 100 serão liberadas
    cem = int(valor_saque / 100)
    valor_saque = valor_saque - (cem * 100)

    # Define quantas notas de 50 serão liberadas
    cinquenta = int(valor_saque / 50)
    valor_saque = valor_saque - (cinquenta * 50)

    # Define quantas notas de 20 serão liberadas
    vinte = int(valor_saque / 20)
    valor_saque = valor_saque - (vinte * 20)

    # Define quantas notas de 10 serão liberadas
    dez = int(valor_saque / 10)
    valor_saque = valor_saque - (dez * 10)

    # Define quantas notas de 5 serão liberadas
    cinco = int(valor_saque / 5)
    valor_saque = valor_saque - (cinco * 5)

    # Define quantas notas de 2 serão liberadas
    dois = int(valor_saque / 2)

    # Mostra resultado
    print('Notas R$100,00 = ', cem)
    print('Notas R$ 50,00 = ', cinquenta)
    print('Notas R$ 20,00 = ', vinte)
    print('Notas R$ 10,00 = ', dez)
    print('Notas R$  5,00 = ', cinco)
    print('Notas R$  2,00 = ', dois)


# Processamento do menu e chamada das funções
if __name__ == '__main__':
    escolha = '0'
    aberta_conta = False
    while escolha != '6':
        if not aberta_conta:
            abrir_conta()
            aberta_conta = True
        else:
            escolha = menu()
        if escolha == '1':
            option_1()
        elif escolha == '2':
            option_2()
        elif escolha == '3':
            option_3()
        elif escolha == '4':
            option_4()
        elif escolha == '5':
            option_5()
        elif escolha == '9':
            print('\nSaindo...\n')
            exit()
        else:
            print('\nOpção desconhecida!\n')

        input('Pressione ENTER para continuar')