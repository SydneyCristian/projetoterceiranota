import time

from usuario import *
from evento import *
from participante import *


def projeto():
    usuarios = {}
    eventos = {}
    participantes = []
    participantes = carregar_participantes(arquivo='participantes.txt')
    usuario_logado = False

    while True:
        if not usuario_logado:
            opcao = menu_usuario()
            if opcao == '0':
                print('Saindo...')
                time.sleep(3)
                break
            if opcao == '1':
                cadastrar_usuario(usuarios)
            if opcao == '2':
                usuario_logado = entrar(usuarios)
        else:
            opcao = menu_evento(usuario_logado)
            if opcao == '0':
                print('Deslogando...')
                time.sleep(3)
                usuario_logado = False
            if opcao == '1':
                cadastrar_evento(eventos, usuario_logado)
            if opcao == '2':
                buscar_evento(eventos, usuario_logado)
            if opcao == '3':
                listar_eventos(eventos, usuario_logado)
            if opcao == '4':
                remover_evento(eventos, usuario_logado)
            if opcao == '5':
                participar_evento(eventos, usuario_logado, participantes)
                salvar_participantes(participantes)
            if opcao == '6':
                listar_participantes(participantes, eventos)
            if opcao == '7':
                valor_arrecadado(eventos, participantes, usuario_logado)
            if opcao == '8':
                avaliar_evento(eventos, usuario_logado, participantes)
            if opcao == '9':
                mostrar_tempo_evento(eventos)


projeto()
