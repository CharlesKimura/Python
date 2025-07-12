from random import choice

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%*'
tamanho = int(input('Quantos caracteres sua senha dever ter? '))
caracteres = minusculas + maiusculas + numeros + simbolos

senha = ''
if tamanho <= 7:
    print('Erro, tamanho deve ser maior que 7')
else:
    for i in range(tamanho):
        senha += choice(caracteres)
    print(f'Senha gerada: {senha}')