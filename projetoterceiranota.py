from usuarios import *
from eventos import *

while True:
    print('+-----------------------------------------------------------------------------+')
    print('+                                 Eventos                                     +')
    print('+                            Mentes Criativas                                 +')
    print('+-----------------------------------------------------------------------------+')
    print('+               [1] - Cadastar novo Usuário                                   +')
    print('+               [2] - Login do Usuário                                        +')
    print('+               [0] - Sair                                                    +')
    print('+-----------------------------------------------------------------------------+')
    opcao = input('Digite uma opção acima: ')

    if opcao == '1':
        novo_usuario(usuarios)
    elif opcao == '0':
        break
    elif opcao == '2':
        login = login_usuario(usuarios)


        while True:
            print('+-----------------------------------------------------------------------------+')
            print(f'                            Bem-vindo(a)!                                     ')
            print('+-----------------------------------------------------------------------------+')
            print('+                                  Eventos                                    +')
            print('+                              Mentes Criativas                               +')
            print('+-----------------------------------------------------------------------------+')
            print('+               [1] - Cadastrar Evento                                        +')
            print('+               [2] - Buscar Evento                                           +')
            print('+               [3] - Listar os eventos                                       +')
            print('+               [4] - Remover eventos                                         +')
            print('+               [5] - Participar de Evento                                    +')
            print('+               [6] - Listar Participantes do evento                          +')
            print('+               [7] - Mostrar valor arrecadado                                +')
            print('+               [8] - Avalie nosso evento                                     +')
            print('+               [9] - Deslogar                                                +')
            print('+-----------------------------------------------------------------------------+')
            opcao = input('Digite uma opção acima: ')
            if opcao == '1':
                cadastrar_evento(eventos)
            elif opcao == '2':
                evento_especifico(eventos)
            elif opcao == '3':
                eventos_totais(eventos)
            elif opcao == '4':
                excluir_evento(eventos)
            elif opcao == '5':
                participar_evento(eventos)
            elif opcao == '6':
                listar_participantes(eventos)
            elif opcao == '7':
                valor_arrecadado(eventos)
            elif opcao == '8':
                avaliar_evento(eventos)
            elif opcao == '9':
                logout_usuario(logado)
                break
    else:
        print('Valor inválido. Tente novamente.')
