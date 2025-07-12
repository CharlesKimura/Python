print('Cadastro de produtos')
produtos = []

while True:
    menu = int(input('''Digite apenas de 1 a 3:
Digite [ 1 ] para cadastrar produtos
Digite [ 2 ] para ver produtos cadastrados
Digite [ 3 ] para sair
Sua escolha: '''))
    
    if menu == 1:
        vezes = int(input('Digite quantos produtos deseja cadastrar: '))
        for c in range(1, vezes + 1):
            produto = input(f'Digite nome do {c}º produto: ')
            quantidade = int(input(f'Digite quantidade do {c}º produto: '))
            item = [produto, quantidade]
            produtos.append(item)
    elif menu == 2:
        if not produtos:
            print('Nenhum produto cadastrado')
        else:
            for item in produtos:
                print(f'Produto: {item[0]} | Quantidade: {item[1]}')
    elif menu == 3:
        print('Programa encerrado')
        break
    else:
        print('Erro, opção inválida')
