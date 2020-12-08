# # Arquivo para testes

# # Convertendo String de ASCII para Binario
# mensagem = "texto claro"

# byte_array = mensagem.encode()
# binary_int = int.from_bytes(byte_array, "big")
# binary_string = bin(binary_int)

# print(binary_string)

# # Convertendo String de Binario para ASCII

# byte_number = binary_int.bit_length() + 7 // 8
# binary_array = binary_int.to_bytes(byte_number, "big")
# ascii_text = binary_array.decode()

# print(ascii_text)

# Recebendo A chave e convertendo p/ uma lista de int

# chave_string = input('Digite a chave: ')
# chave_string = chave_string.split(',')
# chave = []

# for i in range( len(chave_string) ):
#     chave.append(int(chave_string[i]))

# print(chave)

# Convertendo char para binario

caractere = 'b'
cod_ascii = int(ord(caractere))
representacao_binaria = bin(cod_ascii)[2:]
representacao_binaria = representacao_binaria.zfill(8)
print(representacao_binaria)