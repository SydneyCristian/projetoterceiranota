def validar_nome_usuario():
    nome = input('Digite seu nome: ').strip()
    while len(nome) < 4:
        print('O nome de usuário deve possuir mais de 4 caracteres')
        nome = input('Nome inválido. Tente novamente: ')
    return nome


def verificar_caracter(email_usuario):
    if '@' in email_usuario and '.' in email_usuario and len(email_usuario) > 7:
        return email_usuario
    else:
        return False


def validar_email():
    while True:
        print('O e-mail deve conter "@" e "."')
        email_usuario = input('Digite seu e-mail: ')
        if verificar_caracter(email_usuario):
            print('E-mail válido')
            return email_usuario
        if len(email_usuario) == 0:
            print('E-mail invalido, tente novamente.')


def validar_senha():
    senha = input('Digite sua senha: ')
    repetir_senha = input('Digite a senha novamente: ')
    while senha != repetir_senha:
        print('As senhas não correspondem')
        senha = input('Digite a senha novamente: ')
    return senha


def menu_usuario():
    print('+-----------------------------------------------------------------------------+')
    print('+                                 Eventos                                     +')
    print('+                            Mentes Criativas                                 +')
    print('+-----------------------------------------------------------------------------+')
    print('+               [1] - Cadastar novo Usuário                                   +')
    print('+               [2] - Login do Usuário                                        +')
    print('+               [0] - Sair                                                    +')
    print('+-----------------------------------------------------------------------------+')
    opcao = input('Digite uma opção acima: ').strip()
    return opcao


def cadastrar_usuario(usuarios):
    nome = validar_nome_usuario()
    email = validar_email()
    senha = validar_senha()

    if email in usuarios:
        print('Este e-mail já está cadastrado!')
        return usuarios

    usuarios[email] = {'nome': nome, 'email': email, 'senha': senha}
    print('Aguarde processando dados...')
    print('Você foi cadastrado com sucesso!')
    return usuarios


def autenticar_usuario(usuarios, email, senha):
    if email in usuarios and usuarios[email]['senha'] == senha:
        return usuarios[email]
    return False


def entrar(usuarios):
    while True:
        email = input('Digite seu e-mail: ').strip()
        senha = input('Digite sua senha: ').strip()
        if email == '' or senha == '':
            print('E-mail ou senha não podem estar vazios.')
            continue

        usuario_autenticado = autenticar_usuario(usuarios, email, senha)
        if usuario_autenticado:
            print('Logando...')
            print(f'Você está logado como {usuario_autenticado['nome']}')
            return usuario_autenticado
        else:
            print('E-mail ou senha inválidos.')
