login = 'seuemail@seuemail.com'
senha = '12345678'
usuario = input('Digite o usuário: ').strip().lower()
password = input('Digite a senha: ').strip()

if usuario == login and senha == password:
    print('Acesso liberado')
else:
    print('Acesso negado')