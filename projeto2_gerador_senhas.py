from random import choice

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%*'
tamanho = int(input('Quantos caracteres sua senha dever ter? '))
caracteres = minusculas + maiusculas + numeros + simbolos
senha = ''

for i in range(tamanho):
    senha += choice(caracteres)
print(f'Senha gerada: {senha}')