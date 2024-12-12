import matplotlib.pyplot as plt


def novo_participante(eventos, usuario_logado, participantes):
    titulo_evento = input('Digite o nome do evento que você quer participar: ').strip()

    while titulo_evento == '':
        print('O nome do evento não pode ser vazio. Tente novamente.')
        titulo_evento = input('Digite o nome do evento que você quer participar: ').strip()

    evento_encontrado = None
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'] == titulo_evento:
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if evento_encontrado is None:
        print('Evento não encontrado. Tente novamente.')
        return None

    if evento_encontrado['usuario_email'] != usuario_logado['email']:
        print('Você não tem permissão para adicionar participantes a este evento.')
        return

    valor_evento = evento_encontrado['valor']

    while True:
        email_participante = input('Digite o e-mail do participante que deseja adicionar: ').strip()
        nome_participante = input('Digite o nome do participante: ').strip()

        while email_participante == '' and nome_participante == '':
            print('O e-mail ou o nome do participante não pode ser vazio. Tente novamente.')
            email_participante = input('Digite o e-mail do participante que deseja adicionar: ').strip()
            nome_participante = input('Digite o nome do participante: ').strip()

        for participante in participantes:
            if (participante['usuario_email'] == email_participante and
                    participante['evento_email'] == evento_encontrado['usuario_email']):
                print(f'O participante {email_participante} já está inscrito neste evento.')
                return

        participantes.append(
            {'usuario_email': email_participante,
             'nome_evento': titulo_evento,
             'nome_participante': nome_participante,
             'evento_email': evento_encontrado['usuario_email'],
             'valor_a_pagar': valor_evento,
             })

        print(
            f'O participante {nome_participante} ({email_participante}) '
            f'foi adicionado ao evento: {evento_encontrado["titulo"]}. '
            f'O valor a pagar é: R${valor_evento:.2f}')

        continuar = input('Deseja adicionar mais pessoas ao evento? (sim/não): ').strip().lower()

        while continuar not in ['sim', 'não', 's', 'n']:
            continuar = input(
                'Resposta inválida. Deseja adicionar mais pessoas ao evento? (sim/não): ').strip().lower()

        if continuar in ['não', 'n']:
            print('Nenhum outro participante será adicionado.')
            break


def retornar_evento_nome(eventos, evento_email):
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['usuario_email'] == evento_email:
                return evento
    return None


def cancelar_inscricao(eventos, participantes, usuario_logado):
    titulo_evento = input('Digite o título do evento do qual deseja cancelar inscrições: ').strip()

    while titulo_evento == '':
        print('O nome do evento não pode ser vazio. Tente novamente.')
        titulo_evento = input('Digite o título do evento do qual deseja cancelar inscrições: ').strip()

    evento_encontrado = None

    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'] == titulo_evento:
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if evento_encontrado is None:
        print(f'Evento "{titulo_evento}" não encontrado. Tente novamente.')
        return

    if evento_encontrado['usuario_email'] != usuario_logado['email']:
        print('Você não tem permissão para cancelar inscrições neste evento.')
        return

    participantes_inscritos = [
        participante for participante in participantes if
        participante['evento_email'] == evento_encontrado['usuario_email']
    ]

    if not participantes_inscritos:
        print("Não há participantes inscritos nesse evento.")
        return

    print(f'Participantes inscritos no evento {evento_encontrado["titulo"]}:')

    for i, participante in enumerate(participantes_inscritos, start=1):
        print(f'{i}. ({participante["usuario_email"]})')

    email_participante = input('Digite o e-mail do participante que deseja remover: ').strip()
    while email_participante == '':
        print('O e-mail do participante não pode ser vazio. Tente novamente.')
        email_participante = input('Digite o e-mail do participante que deseja remover: ').strip()

    participante_encontrado = None
    for participante in participantes_inscritos:
        if participante['usuario_email'] == email_participante:
            participante_encontrado = participante
            break

    if participante_encontrado is None:
        print(f'Nenhum participante com o e-mail {email_participante} encontrado.')
        return

    continuar = input(
        f'Deseja realmente remover o participante {participante_encontrado["usuario_email"]} (sim/não)? ').strip().lower()

    while continuar not in ['sim', 'não', 's', 'n']:
        continuar = input('Resposta inválida. Deseja realmente remover esse participante? (sim/não): ').strip().lower()

    if continuar in ['sim', 's']:
        participantes.remove(participante_encontrado)
        print(f'A inscrição do participante {participante_encontrado["usuario_email"]} será cancelada.')
    else:
        print('Cancelamento de inscrição abortado.')

    print('Processo de cancelamento de inscrição concluído.')


def participar_evento_criador(eventos, participantes, usuario_logado):
    titulo_evento = input('Digite o título do evento no qual deseja se inscrever: ')

    while titulo_evento == '':
        print('O título do evento não pode ser vazio. Tente novamente.')
        titulo_evento = input('Digite o título do evento no qual deseja se inscrever: ')

    evento_encontrado = None
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'] == titulo_evento:
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if evento_encontrado is None:
        print('Evento não encontrado.')
        return

    for participante in participantes:
        if participante['usuario_email'] == usuario_logado['email'] and participante['evento_email'] == \
                evento_encontrado['usuario_email']:
            print(f'Você já está inscrito no evento: {evento_encontrado["titulo"]}')
            return

    participantes.append({
        'usuario_email': usuario_logado['email'],
        'evento_email': evento_encontrado['usuario_email']
    })
    print(f'Você foi inscrito com sucesso no evento: {evento_encontrado["titulo"]}')


def validar_opcao_participante():
    print('Escolha uma opção: ')
    print('[1] - Novo Participante')
    print('[2] - Cancelar inscrição')
    print('[3] - Participar do evento')
    print('[0] - Voltar')
    opcao = input('Opção: ')

    while opcao not in ['0', '1', '2', '3']:
        print('Opção inválida.')
        print('Escolha uma opção: ')
        print('[1] - Novo Participante')
        print('[2] - Cancelar inscrição')
        print('[3] - Participar do evento')
        print('[0] - Voltar')
        opcao = input('Opção: ')
    return opcao


def participar_evento(eventos, usuario_logado, participantes):
    opcao = validar_opcao_participante()
    if opcao == '0':
        return None
    if opcao == '1':
        novo_participante(eventos, usuario_logado, participantes)
    if opcao == '2':
        cancelar_inscricao(eventos, participantes, usuario_logado)
    if opcao == '3':
        participar_evento_criador(eventos, participantes, usuario_logado)


def listar_participantes(participantes, eventos):
    titulo_evento = input('Digite o título do evento para listar os participantes: ')

    while titulo_evento == '':
        print('O título do evento não pode ser vazio. Tente novamente.')
        titulo_evento = input('Digite o título do evento para listar os participantes: ')

    evento_encontrado = None
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'] == titulo_evento:
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if evento_encontrado is None:
        print('Evento não encontrado.')
        return

    print(f'\nParticipantes do evento "{evento_encontrado["titulo"]}":')

    participantes_do_evento = [participante for participante in participantes
                               if participante['evento_email'] == evento_encontrado['usuario_email']]

    if not participantes_do_evento:
        print('Nenhum participante encontrado para este evento.')
    else:
        for participante in participantes_do_evento:
            print(f'Participante: {participante["usuario_email"]}')

    print('\nDeseja ver o gráfico com o total de participantes?')
    print('Escolha uma opção: ')
    print('[1] - Sim')
    print('[2] - Não')
    opcao = input('Escolha uma opção: ')

    while opcao not in ['1', '2']:
        print('Opção inválida')
        print('Escolha uma opção: ')
        print('[1] - Sim')
        print('[2] - Não')
        opcao = input('Escolha uma opção: ')

    if opcao == '2':
        print('Saindo...')
        return

    if opcao == '1':
        eventos_contagem = {}
        for participante in participantes:
            evento_email = participante['evento_email']
            if evento_email in eventos_contagem:
                eventos_contagem[evento_email] += 1
            else:
                eventos_contagem[evento_email] = 1

        eventos_nomes = []
        participantes_por_evento = []

        for lista_eventos in eventos.values():
            for evento in lista_eventos:
                eventos_nomes.append(evento['titulo'])
                participantes_por_evento.append(eventos_contagem.get(evento['usuario_email'], 0))

        plt.bar(eventos_nomes, participantes_por_evento, color='blue')

        plt.title('Número de Participantes por Evento')
        plt.xlabel('Eventos')
        plt.ylabel('Número de Participantes')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()


def valor_arrecadado(eventos, participantes, usuario_logado):
    titulo_evento = input('Digite o nome do evento para ver o valor arrecadado: ').strip()

    while titulo_evento == '':
        print('O nome do evento não pode ser vazio. Tente novamente.')
        titulo_evento = input('Digite o nome do evento para ver o valor arrecadado: ').strip()

    evento_encontrado = None
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'] == titulo_evento:
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if evento_encontrado is None:
        print('Evento não encontrado. Tente novamente.')
        return

    if evento_encontrado['usuario_email'] != usuario_logado['email']:
        print('Você não tem permissão para ver os dados financeiros deste evento.')
        return

    participantes_evento = [
        participante for participante in participantes
        if participante['evento_email'] == evento_encontrado['usuario_email']
    ]

    valor_evento = evento_encontrado['valor']
    total_arrecadado = len(participantes_evento) * valor_evento

    if len(participantes_evento) > 0:
        valor_por_participante = total_arrecadado / len(participantes_evento)
    else:
        valor_por_participante = 0

    print(f'\nEvento: {evento_encontrado["titulo"]}')
    print(f'Criador do Evento: {evento_encontrado["usuario_email"]}')
    print(f'Valor total arrecadado: R${total_arrecadado:.2f}')
    print(f'Número de participantes: {len(participantes_evento)}')
    print(f'Valor por participante: R${valor_por_participante:.2f}')

    print('\nParticipantes cadastrados e pagos no evento:')
    if not participantes_evento:
        print('Nenhum participante inscrito.')


def carregar_participantes(arquivo='participantes.txt'):
    participantes = []
    try:
        with open(arquivo, 'r') as file:
            for linha in file:
                dados = linha.strip().split('|')
                if len(dados) == 5:
                    participante = {
                        'usuario_email': dados[0],
                        'nome_evento': dados[1],
                        'nome_participante': dados[2],
                        'evento_email': dados[3],
                        'valor_a_pagar': float(dados[4]),
                    }
                    participantes.append(participante)
    except FileNotFoundError:
        print('Arquivo de participantes não encontrado. Nenhum participante carregado.')
    return participantes

def salvar_participantes(participantes, arquivo='participantes.txt'):
    with open(arquivo, 'w') as file:
        for participante in participantes:
            linha = f"{participante['usuario_email']}|{participante['nome_evento']}|{participante['nome_participante']}|{participante['evento_email']}|{participante['valor_a_pagar']}\n"
            file.write(linha)

