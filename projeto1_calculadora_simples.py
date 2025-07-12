try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    operador = int(input('''Digite apenas números de 1 a 4
Digite [ 1 ] para somar
Digite [ 2 ] para subtrair
Digite [ 3 ] para multiplicar
Digite [ 4 ] para dividir
Sua escolha: '''))

    resultado = None
    operacao = ''
    if operador == 1:
        resultado = numero1 + numero2
        operacao = 'Soma'
    elif operador == 2:
        resultado = numero1 - numero2
        operacao = 'Subtração'
    elif operador == 3:
        resultado = numero1 * numero2
        operacao = 'Multiplicação'
    elif operador == 4:
        resultado = numero1 / numero2
        operacao = 'Divisão'
    else:
        print('Opção inválida')
    
    if resultado is not None:
        print(f'A {operacao} é {resultado}')

except ValueError:
    print('Erro, digite apenas números')
