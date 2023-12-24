"""
Придумать и написать шифровальщик текста
Он будет принимать строку и ключ шифрования, возвращать ее в зашифрованном виде
Затем должен быть дешифровальщик который пример зашифрованную строку и ключ и расшифрует ее
"""

"""Всем привет -> Жцйс фхнжйч -> Всем привет"""  # Придумать что-то интереснее шифра Цезаря
def encrypt(text, key):


    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) + key)
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_char = chr(ord(char) - key)
        decrypted_text += decrypted_char
    return decrypted_text


# Пример использования

text = "Привет, мир!"
key = 5

encrypted_text = encrypt(text, key)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Расшифрованный текст:", decrypted_text)
