usuarios = {}


def validar_nome_usuario(usuarios):
    nome = input('Digite seu nome: ')
    while len(nome) < 4:
        print('O nome de usário deve possuir mais de 4 caracteres')
        nome = input('Nome inválido. Digite novamente: ')
    return nome


def verificar_caracter(email_usuario):
    if '@' in email_usuario and '.' in email_usuario and len(email_usuario) > 7:
        return email_usuario
    else:
        return False


def verificar_email(email_usuario):
    while True:
        print('O e-mail deve conter "@" e ".".')
        email_usuario = input('Digite seu e-mail: ')
        if verificar_caracter(email_usuario):
            print('E-mail válido')
            return email_usuario
        if len(email_usuario) == 0:
            print('E-mail invalido, tente novamente.')


def validar_senha(usuarios):
    senha = input('Digite sua senha: ')
    repetir_senha = input('Digite a senha novamente: ')
    while senha != repetir_senha:
        print('As senhas não correspondem')
        senha = input('Digite a senha: ')
        repetir_senha = input('Digite a senha novamente: ')
    return senha


def novo_usuario(usuarios):  # 1 OK
    nome = validar_nome_usuario(usuarios)
    email = verificar_email(usuarios)
    senha = validar_senha(usuarios)
    usuario = [email, senha]
    usuarios[nome] = usuario
    print('Usuário cadastrado com sucesso')
    return usuario


def retornar_usuario(email, senha):
    for nome in usuarios:
        dados = usuarios[nome]
        if dados[0] == email and dados[1] == senha:
            return nome
    return False


def login_usuario(usuarios):
    while True:
        email_usuario = input('Digite seu e-mail: ')
        senha_usuario = input('Digite sua senha: ')
        if email_usuario == '' or senha_usuario == '':
            print('E-mail ou senha não podem estar vazios.')
            continue
        usuario = retornar_usuario(email_usuario, senha_usuario)
        if usuario:
            print(f'Você está logado como {usuario}.')
            return usuario
        else:
            print('Usuário ou senha inválidos.')


def logout_usuario(logado):
    if logado:
        print('Você foi deslogado com sucesso.')
        return False
    else:
        print('Você não está logado.')
        return logado
