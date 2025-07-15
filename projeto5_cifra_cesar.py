# Solicita ao usuário uma mensagem para cifrar
texto = input('Digite uma mensagem para cifrar: ')
# Define o valor do deslocamento da cifra de César
deslocamento = 3

# Função que aplica a cifra de César
def cifra_cesar(mensagem, desloc):
    # Define o alfabeto utilizado
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    # Inicializa a string do texto cifrado
    texto_cifrado = ''

    # Percorre cada caractere da mensagem (em minúsculo)
    for caractere in mensagem.lower():
        if caractere == ' ':  # Mantém os espaços
            texto_cifrado += caractere
        else:
            # Encontra o índice do caractere no alfabeto
            indice = alfabeto.find(caractere)
            # Calcula o novo índice com o deslocamento
            novo_indice = (indice + desloc) % len(alfabeto)
            # Adiciona o novo caractere cifrado
            texto_cifrado += alfabeto[novo_indice]
    # Exibe o texto original
    print('texto original:', mensagem)
    # Exibe o texto cifrado
    print('texto cifrado:', texto_cifrado)

# Chama a função com deslocamento 3
cifra_cesar(texto, deslocamento)
# Chama a função com deslocamento 13 (ROT13)
cifra_cesar(texto, 13)