# Arquivo para testes

# Convertendo String de ASCII para Binario
mensagem = "texto claro"

byte_array = mensagem.encode()
binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)

print(binary_string)

# Convertendo String de Binario para ASCII

byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()

print(ascii_text)