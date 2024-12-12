def validar_titulo():
    titulo = input('Digite o titulo do evento: ').strip()
    while len(titulo) < 4:
        print('O titulo do evento deve possuir mais de 4 caracteres')
        titulo = input('Título inválido. Digite novamente: ').strip()
    return titulo


def validar_descricao():
    descricao = input('Digite a descrição do evento: ').strip()
    while len(descricao) < 4:
        print('A descrição do evento deve possuir mais de 4 caracteres')
        descricao = input('Descrição inválida. Digite novamente: ').strip()
    return descricao


import re


def validar_data():
    while True:
        data = input('Digite a data do evento (formato DD/MM/AAAA): ').strip()
        if re.match(r'^\d{2}/\d{2}/\d{4}$', data):
            dia, mes, ano = map(int, data.split('/'))
            if mes < 1 or mes > 12:
                print('Mês inválido! O mês deve estar entre 01 e 12. Tente novamente.')
                continue
            if ano < 1900 or ano > 2100:
                print('Ano inválido! O ano deve estar entre 1900 e 2100. Tente novamente.')
                continue
            dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                dias_no_mes[1] = 29
            if dia < 1 or dia > dias_no_mes[mes - 1]:
                print(f'Dia inválido! O mês {mes} tem no máximo {dias_no_mes[mes - 1]} dias. Tente novamente.')
                continue
            return data
        else:
            print('Formato inválido! A data deve ser no formato DD/MM/AAAA. Tente novamente.')


def validar_local():
    local = input('Digite o local do evento: ').strip()
    while len(local) < 4:
        print('O local do evento deve possuir mais de 4 caracteres')
        local = input('Local inválido. Digite novamente: ').strip()
    return local


def validar_valor():
    valor = float(input('Digite o valor da incrição do evento: '))
    while valor <= 0.0:
        print('O valor da incrição do evento deve ser maior que R$ 0,00')
        valor = float(input('Valor inválido. Digite novamente: '))
    return valor


def validar_tipo():
    print('Escolha o status do evento: ')
    print('[1] - Privado')
    print('[2] - Público')
    status = input('Opção: ').strip()
    while status != '1' and status != '2':
        print('Opção inválida. Escolha entre Privado ou Público')
    if status == '1':
        return 'privado'
    if status == '2':
        return 'publico'


def menu_evento(usuario_logado):
    print('+-----------------------------------------------------------------------------+')
    print('+                               Bem-vindo(a)!                                 +')
    print(f'                                 "{usuario_logado['nome']}"')
    print('+-----------------------------------------------------------------------------+')
    print('+                                  Eventos                                    +')
    print('+                              Mentes Criativas                               +')
    print('+-----------------------------------------------------------------------------+')
    print('+               [1] - Cadastrar Evento                                        +')
    print('+               [2] - Buscar Evento                                           +')
    print('+               [3] - Listar os evento                                        +')
    print('+               [4] - Remover evento                                          +')
    print('+               [5] - Participar de Evento                                    +')
    print('+               [6] - Listar Participantes do evento                          +')
    print('+               [7] - Mostrar valor arrecadado                                +')
    print('+               [8] - Avalie nosso evento                                     +')
    print('+               [9] - Tempo Restante                                          +')
    print('+               [0] - Deslogar                                                +')
    print('+-----------------------------------------------------------------------------+')
    opcao = input('Digite uma opção acima: ').strip()
    return opcao


def cadastrar_evento(eventos, usuario_logado):
    titulo = validar_titulo()
    descricao = validar_descricao()
    data = validar_data()
    local = validar_local()
    valor = validar_valor()
    status = validar_tipo()

    evento = {
        'titulo': titulo,
        'descricao': descricao,
        'data': data,
        'local': local,
        'valor': valor,
        'usuario_email': usuario_logado['email'],
        'status': status
    }
    if usuario_logado['email'] not in eventos:
        eventos[usuario_logado['email']] = []

    eventos[usuario_logado['email']].append(evento)
    print('Evento criado com sucesso!')

    return eventos


def filtrar_eventos(eventos, titulo, data, local, status, usuario_email):
    eventos_filtrados = []

    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if (
                    (titulo == '' or evento['titulo'].lower() == titulo.lower()) and
                    (data == '' or evento['data'] == data) and
                    (local == '' or evento['local'].lower() == local.lower()) and
                    (status == '' or evento['status'].lower() == status.lower())
            ):
                eventos_filtrados.append(evento)
    return eventos_filtrados


from tabulate import tabulate


def buscar_evento(eventos, usuario_logado):
    global headers
    print('Escolha o filtro de busca: ')
    print('[1] - Título')
    print('[2] - Data')
    print('[3] - Local')
    opcao = input('Opção: ').strip()

    while opcao not in ['1', '2', '3']:
        print('Opção inválida. Escolha entre as opções:')
        print('[1] - Título')
        print('[2] - Data')
        print('[3] - Local')
        opcao = input('Opção: ').strip()

    eventos_publicos = []
    eventos_privados = []

    if opcao == '1':
        titulo = input('Digite o termo de pesquisa do título: ').strip()
        eventos_publicos = filtrar_eventos(eventos, titulo, '', '', 'publico', '')
        eventos_privados = filtrar_eventos(eventos, titulo, '', '', 'privado', usuario_logado['email'])

    elif opcao == '2':
        data = input('Digite o termo de pesquisa da data (formato DD/MM/AAAA): ').strip()
        eventos_publicos = filtrar_eventos(eventos, '', data, '', 'publico', '')
        eventos_privados = filtrar_eventos(eventos, '', data, '', 'privado', usuario_logado['email'])

    elif opcao == '3':
        local = input('Digite o termo de pesquisa do local: ').strip()
        eventos_publicos = filtrar_eventos(eventos, '', '', local, 'publico', '')
        eventos_privados = filtrar_eventos(eventos, '', '', local, 'privado', usuario_logado['email'])

    if eventos_publicos:
        print("\nEventos Públicos Encontrados:")
        headers = ['Título', 'Data', 'Local', 'Status', 'Valor Inscrição']
        table_publicos = [
            [evento['titulo'], evento['data'], evento['local'], evento['status'], f'R$ {evento["valor"]:.2f}'] for
            evento in eventos_publicos]
        print(tabulate(table_publicos, headers, "grid"))
    else:
        print('Nenhum evento público encontrado com esse filtro.')

    if eventos_privados:
        print("\nEventos Privados Encontrados:")
        table_privados = [
            [evento['titulo'], evento['data'], evento['local'], evento['status'], f'R$ {evento["valor"]:.2f}'] for
            evento in eventos_privados]
        print(tabulate(table_privados, headers, "grid"))
    else:
        print('Nenhum evento privado encontrado com esse filtro.')


def exibir_evento_menu(evento):
    print("+-----------------------------------------------------------------------------+")
    print(f"Evento: {evento['titulo']}")
    print("+-----------------------------------------------------------------------------+")
    print(f"Título: {evento['titulo']}")
    print(f"Data: {evento['data']}")
    print(f"Local: {evento['local']}")
    print(f"Status: {evento['status']}")
    print(f"Valor da Inscrição: R$ {evento['valor']:.2f}")
    print(f"Descrição: {evento['descricao']}")
    print("+-----------------------------------------------------------------------------+")


def listar_eventos(eventos, usuario_logado):
    print('Escolha o status de listagem: ')
    print('[1] - Todos')
    print('[2] - Por usuário')
    opcao = input('Opção: ').strip()
    while opcao not in ['1', '2']:
        print('Opção inválida. Escolha o status de listagem: ')
        print('[1] - Todos')
        print('[2] - Por usuário')
        opcao = input('Opção: ').strip()

    if opcao == '1':
        eventos_publicos = []
        eventos_privados = []
        for usuario, lista_eventos in eventos.items():
            for evento in lista_eventos:
                if evento['status'] == 'publico':
                    eventos_publicos.append(evento)
                elif evento['status'] == 'privado' and usuario == usuario_logado['email']:
                    eventos_privados.append(evento)
        print("+-----------------------------------------------------------------------------+")
        print("Eventos Públicos:")
        for evento in eventos_publicos:
            exibir_evento_menu(evento)
        print("+-----------------------------------------------------------------------------+")
        print("Eventos Privados:")
        for evento in eventos_privados:
            exibir_evento_menu(evento)
        print("+-----------------------------------------------------------------------------+")

    if opcao == '2':
        usuario_email = input('Digite o e-mail do usuário: ').strip()

        while usuario_email == '':
            print('O e-mail não pode ser vazio. Tente novamente.')
            usuario_email = input('Digite o e-mail do usuário: ').strip()

        if usuario_email == usuario_logado['email']:
            meus_eventos = eventos.get(usuario_email, [])
            print("+-----------------------------------------------------------------------------+")
            print(f"Meus eventos ({usuario_email}):")
            for evento in meus_eventos:
                exibir_evento_menu(evento)
            print("+-----------------------------------------------------------------------------+")
        else:
            eventos_publicos = []
            for evento in eventos.get(usuario_email, []):
                if evento['status'] == 'publico':
                    eventos_publicos.append(evento)
            print("+-----------------------------------------------------------------------------+")
            print(f"Eventos Públicos do usuário {usuario_email}:")
            for evento in eventos_publicos:
                exibir_evento_menu(evento)
            print("+-----------------------------------------------------------------------------+")


def remover_evento(eventos, usuario_logado):
    titulo_evento = input('Digite o título do evento que deseja remover: ').strip()

    while titulo_evento == '':
        print('O título do evento não pode ser vazio. Tente novamente.')
        titulo_evento = input('Digite o título do evento que deseja remover: ').strip()

    evento_encontrado = False
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'].lower() == titulo_evento.lower():
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if not evento_encontrado:
        print(f'Evento com o título "{titulo_evento}" não encontrado.')
        return

    if evento_encontrado['usuario_email'] != usuario_logado['email']:
        print('Você não é o criador deste evento, portanto não pode removê-lo.')
        return

    print(f'Você realmente deseja remover o evento "{titulo_evento}"? ([1]-sim/[2]-não): ')
    print('Escolha uma opção: ')
    print('[1] - Sim')
    print('[2] - Não')
    opcao = input('Escolha uma opção: ')

    while opcao not in ['1', '2']:
        opcao = input(f'Você realmente deseja remover o evento "{titulo_evento}"? (sim/não): ').strip().lower()

    if opcao == '1':

        for usuario_email, lista_eventos in eventos.items():
            for i, evento in enumerate(lista_eventos):
                if evento['titulo'].lower() == titulo_evento.lower():
                    del lista_eventos[i]
                    print(f'O evento "{titulo_evento}" foi removido com sucesso!')
                    return
    if opcao == '2':
        print(f'A remoção do evento "{titulo_evento}" foi cancelada.')
    return opcao


def avaliar_evento(eventos, usuario_logado, participantes):
    global evento, organizacao, local, atracoes, media
    nome_evento = input('Digite o título do evento que deseja avaliar: ').strip()

    while nome_evento == '':
        print('O título do evento não pode ser vazio. Tente novamente.')
        nome_evento = input('Digite o título do evento que deseja avaliar: ').strip()

    evento_encontrado = None
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'].lower() == nome_evento.lower():
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if evento_encontrado is None:
        print(f'Evento "{nome_evento}" não encontrado.')
        return

    is_participante = False
    for participante in participantes:
        if (participante['usuario_email'] == usuario_logado['email'] and
                participante['evento_email'] == evento_encontrado['usuario_email']):
            is_participante = True
            break

    if not is_participante:
        print('Você precisa estar inscrito no evento para avaliá-lo.')
        return
    while True:
        print('Avaliação do Evento (As notas devem estar entre 0 e 10)')
        try:
            organizacao = float(input('Como você avalia a organização do evento: '))
            local = float(input('Como você avalia o local do evento: '))
            atracoes = float(input('Como você avalia as atrações do evento: '))
        except ValueError:
            print('Entrada inválida. Por favor, insira um número entre 0 e 10.')
            continue

        if 0 <= organizacao <= 10 and 0 <= local <= 10 and 0 <= atracoes <= 10:
            total = organizacao + local + atracoes
            media = total / 3
            print(f'A nota final do evento é: {media:.1f}')
            break
        else:
            if organizacao < 0 or local < 0 or atracoes < 0:
                print('Notas não podem ser negativas. Tente novamente.')
            else:
                print('As notas devem estar entre 0 e 10. Tente novamente.')

    if 'avaliacoes' not in evento:
        evento['avaliacoes'] = []

    evento['avaliacoes'].append({
        'usuario_email': usuario_logado['email'],
        'nota_organizacao': organizacao,
        'nota_local': local,
        'nota_atracoes': atracoes,
        'media': media
    })

    if media == 10:
        print('5 estrelas (⭐⭐⭐⭐⭐)')
    elif 9 <= media < 10:
        print('4,5 estrelas (⭐⭐⭐⭐*)')
    elif 8 <= media < 9:
        print('4 estrelas (⭐⭐⭐⭐)')
    elif 7 <= media < 8:
        print('3,5 estrelas (⭐⭐⭐*)')
    elif 6 <= media < 7:
        print('3 estrelas (⭐⭐⭐)')
    elif 5 <= media < 6:
        print('2,5 estrelas (⭐⭐*)')
    elif 4 <= media < 5:
        print('2 estrelas (⭐⭐)')
    elif 3 <= media < 4:
        print('1,5 estrelas (⭐*)')
    elif 2 <= media < 3:
        print('1 estrela (⭐)')
    elif 1 <= media < 2:
        print('0,5 estrela (*)')
    else:
        print('Nenhuma estrela')

    medias = [avaliacao['media'] for avaliacao in evento['avaliacoes']]
    evento['media_geral'] = sum(medias) / len(medias)
    print(f'A média geral do evento agora é: {evento["media_geral"]:.1f}')


from datetime import datetime


def mostrar_tempo_evento(eventos):
    evento_nome = input('Digite o nome do evento para ver o tempo restante: ').strip()

    while evento_nome == '':
        print('O nome do evento não pode ser vazio. Tente novamente.')
        evento_nome = input('Digite o nome do evento para ver o tempo restante: ')

    evento_encontrado = None
    for lista_eventos in eventos.values():
        for evento in lista_eventos:
            if evento['titulo'] == evento_nome:
                evento_encontrado = evento
                break
        if evento_encontrado:
            break

    if not evento_encontrado:
        print('Evento não encontrado')
        return

    evento = evento_encontrado

    data_evento_str = evento['data']

    try:
        data_evento_str = data_evento_str + ' 00:00:00'

        data_evento = datetime.strptime(data_evento_str, "%d/%m/%Y %H:%M:%S")

    except ValueError as e:
        print(f'Erro ao converter a data: {e}')
        return

    data_atual = datetime.now()

    tempo_restante = data_evento - data_atual
    if tempo_restante.total_seconds() > 0:
        dias = tempo_restante.days
        horas, resto = divmod(tempo_restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)
        print(f'Tempo restante para o evento {evento["titulo"]}: ')
        print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')
    else:
        print(f'O evento {evento["titulo"]} já ocorreu ou está em andamento.')
