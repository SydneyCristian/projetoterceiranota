eventos = {}
participar = []
def validar_nome_evento(eventos):
    nome_evento = input('Digite o nome do evento: ')
    while len(nome_evento) < 4:
        print('O nome do evento deve possuir mais de 4 caracteres.')
        nome_evento = input('Nome inválido. Digite o nome novamente: ')
    return nome_evento


def validar_descricao(eventos):
    descricao = input('Digite a descrição do evento: ')
    while len(descricao) < 4:
        print('A descrição do evento deve possuir mais de 4 caracteres.')
        descricao = input('Descrição inválida. Digite a descrição novamente: ')
    return descricao


def validar_data(eventos):
    data = input('Digite a data do evento DD/MM/AAAA: ')
    while len(data) < 10:
        print('A data do evento deve possuir mais de 10 caracteres.')
        data = input('Data inválida. Digite novamente:  ')
    return data

def validar_valor(eventos):
    valor = float(input('Digite o valor da incrição do evento: '))
    while valor <= 0:
        print('O valor de incrição do evento deve ser mair que R$0,00')
        valor = float(input('Valor inválido. Digite novamente: '))
    return valor

def validar_local(eventos):
    local = input('Digite o local do evento: ')
    while len(local) < 4:
        print('O local do evento deve possuir mais de 4 caracteres.')
        local = input('Local inválido. Digite novamente: ')
    return local

def cadastrar_evento(eventos):
    nome = validar_nome_evento(eventos)
    descricao = validar_descricao(eventos)
    data = validar_data(eventos)
    local = validar_local(eventos)
    valor = validar_valor(eventos)
    informacoes = [descricao,data,local,valor]
    eventos[nome] = informacoes
    print('Evento cadastrado com sucesso!')

def excluir_evento(eventos):  # 6 OK
    busca = input('Digite o nome do evento para remover: ')
    for evento in eventos:
        if busca == evento[0]:
            pergunta = input('Qual o nome da pessoa que cadastrou o evento: ')
            if evento[1] == pergunta:
                eventos.remove(evento)
                print('Evento excluído com sucesso!')
                return
            else:
                print('Você não é o dono do evento')
                return
    else:
        print('Evento não encontrado')

def evento_especifico(eventos):
    evento = input('Digite o nome de um evento: ')
    evento_encontrado = False
    for i in eventos:
        dados = eventos[i]
        if i == evento:
             print(f'{evento} está na lista')
        else:
            print('Esse evento não está na lista')

def eventos_totais(eventos):
    if eventos:
        for buscar_evento in eventos:
            print(buscar_evento)
    else:
        print("A lista de eventos está vazia.")

def participar_evento(eventos):
    evento = input('Digite o nome do evento que você quer participar: ')
    for i in eventos:
        if evento == i[0]:
            nome = input('Qual o seu nome: ')
            participar.append([i[0], nome])
            print(f'Você está inscrito no evento {i[0]} com sucesso!')
            return evento

def listar_participantes(eventos):
    evento = input('Qual evento você quer ver os participantes: ')
    evento_encontrado = False
    for i in eventos:
        if i[0] == evento:
            evento_encontrado = True
    if evento_encontrado:
        participantes_encontrados = []
        for i in participar:
            if i[0] == evento:
                participantes_encontrados.append(i[1])
        if participantes_encontrados:
            print(f'Participantes do evento "{evento}":')
            for participante in participantes_encontrados:
                print(participante)
        else:
            print(f'A lista de participantes do evento "{evento}" está vazia.')
    else:
        print(f'O evento "{evento}" não foi encontrado.')


def valor_arrecadado(eventos):
    evento_nome = input('Digite o nome do evento para ver a arrecadação: ')
    evento_encontrado = False
    inscritos = 0
    total_arrecadado = 0
    for evento in eventos:
        if evento[0] == evento_nome:
            evento_encontrado = True
            valor_inscricao = evento[5]
            for i in participar:
                if i[0] == evento_nome:
                    inscritos += 1
                    total_arrecadado = valor_inscricao * inscritos
            print(f'Valor total arrecadado para o evento "{evento_nome}": R$ {total_arrecadado:.2f}')
            return
    if not evento_encontrado:
        print('Evento não encontrado!')

def avaliar_evento(eventos):
    evento_especifico(eventos)
    while True:
        print('Avaliação do Evento (As notas devem estar entre 0 e 10)')
        organizacao = float(input('Como você avalia a organização do evento: '))
        local = float(input('Como você avalia o local do evento: '))
        atracoes = float(input('Como você avalia as atrações do evento: '))

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
        print('nenhuma estrela')
        eventos.append([media])
