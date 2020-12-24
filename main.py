# Trabalho de Topicos Avancados - Criptografia

def representacao_numerica(letra):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    for i in range(len(alfabeto)):
        if letra == alfabeto[i]:
            return i
    return -1


def cifrar_letra_vigenere(letra, chave):
    matriz = [
        ['a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b'],
        ['b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c'],
        ['c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd'],
        ['d', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e'],
        ['e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f'],
        ['f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g'],
        ['g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h'],
        ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i'],
        ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j'],
        ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k'],
        ['k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l'],
        ['l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm'],
        ['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n'],
        ['n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o'],
        ['o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p'],
        ['p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q'],
        ['q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r'],
        ['r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
        ['s', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't'],
        ['t', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v', 'u'],
        ['u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w', 'v'],
        ['v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x', 'w'],
        ['w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y', 'x'],
        ['x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z', 'y'],
        ['y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ', 'z'],
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' '],
        [' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    ]

    coluna = representacao_numerica(letra)
    return matriz[chave][coluna]


def formatar_chave(chave_string):
    chave_formatada = []
    chave_string = chave_string.split(',')

    for i in range(len(chave_string)):
        chave_formatada.append(int(chave_string[i]))

    return chave_formatada

def posicao_na_chave(chave, numero):
    for i in range(len(chave)):
        if chave[i] == numero:
            return i


def operador_xor(caractere, algarismo_chave):
    cod_ascii = int(ord(caractere))

    representacao_binaria_caractere = bin(cod_ascii)[2:].zfill(8)
    representacao_binaria_algarismo = bin(algarismo_chave)[2:].zfill(8)
    resultado = ""

    i = 0
    while i < 8:
        if representacao_binaria_caractere[i] != representacao_binaria_algarismo[i]:
            resultado = resultado + "1"
        else:
            resultado = resultado + "0"
        i += 1

    resultado_inteiro = int(resultado, 2)
    return chr(resultado_inteiro)


def quebrar_string_chunks(mensagem, tamanho_chunk):
    chunks = []

    tamanho_mensagem = len(mensagem)
    total_chunks = int(tamanho_mensagem / tamanho_chunk)

    if tamanho_mensagem % tamanho_chunk != 0:
        total_chunks += 1

    cont = 0
    i = 0
    j = tamanho_chunk

    while cont < total_chunks:
        chunks.append(mensagem[i:j])
        i += tamanho_chunk
        j += tamanho_chunk
        cont += 1

    ultimo = len(chunks) - 1
    if len(chunks[ultimo]) < tamanho_chunk:
        chunk = chunks[ultimo]
        while len(chunk) < tamanho_chunk:
            chunk = chunk + " "

        chunks[ultimo] = chunk

    return chunks


def cifra_cerca_trilho(mensagem, chave):
    saida = ""
    tamanho_chave = len(chave)
    chunks = quebrar_string_chunks(mensagem, tamanho_chave)

    cont = 1
    while cont <= tamanho_chave:
        coluna = posicao_na_chave(chave, cont)
        for chunk in chunks:
            saida = saida + chunk[coluna]

        cont += 1

    return saida


def cifra_polialfabetica(mensagem, chave):
    saida = ""
    tamanho_chave = len(chave)
    chunks = quebrar_string_chunks(mensagem, tamanho_chave)

    for chunk in chunks:
        for i in range(len(chunk)):
            letra = chunk[i]
            letra_cifrada = cifrar_letra_vigenere(letra, chave[i])
            saida = saida + letra_cifrada

    return saida


def cifra_fluxo(mensagem, chave):
    saida = ""
    tamanho_chave = len(chave)

    for i in range(len(mensagem)):
        posicao = i % tamanho_chave
        resultado = operador_xor(mensagem[i], chave[posicao])
        saida = saida + resultado

    return saida


mensagem = input()
chave = input()

chave = formatar_chave(chave)
tamanho_chave = len(chave)

mensagem = cifra_cerca_trilho(mensagem, chave)

mensagem = cifra_polialfabetica(mensagem, chave)

mensagem = cifra_fluxo(mensagem, chave)
print(mensagem)
