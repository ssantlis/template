def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Шифрует открытый текст с помощью шифра Виженера.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    keyword = keyword.upper()  #Приводим ключ к верхнему регистру для унификации
    plaintext = plaintext.upper()  #Приводим открытый текст к верхнему регистру
    ciphertext = []  #Список для хранения зашифрованных символов
    keyword_length = len(keyword)  #Определяем длину ключа

    keyword_index = 0  #Индекс для отслеживания текущего символа ключа в процессе шифрования
    for char in plaintext:  #Проходим по каждому символу открытого текста
        if char.isalpha():  #Проверяем, является ли символ алфавитным
            shift = ord(keyword[keyword_index % keyword_length]) - ord('A')  #Вычисляем сдвиг по ключу
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))  #Шифруем символ
            ciphertext.append(encrypted_char)  #Добавляем зашифрованный символ в список
            keyword_index += 1  #Переходим к следующему символу ключа
        else:
            ciphertext.append(char)  #Если символ не алфавитный, добавляем его без изменений

    return ''.join(ciphertext)  #Возвращаем зашифрованный текст в виде строки ('' - без разделителей)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Расшифровывает зашифрованный текст с помощью шифра Виженера.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword = keyword.upper()  #Приводим ключ к верхнему регистру
    ciphertext = ciphertext.upper()  #Приводим зашифрованный текст к верхнему регистру
    plaintext = []  #Список для хранения расшифрованных символов
    keyword_length = len(keyword)  #Определяем длину ключа

    keyword_index = 0  #Индекс для отслеживания текущего символа ключа в процессе расшифровки
    for char in ciphertext:  #Проходим по каждому символу зашифрованного текста
        if char.isalpha():  #Проверяем, является ли символ алфавитным
            shift = ord(keyword[keyword_index % keyword_length]) - ord('A')  #Вычисляем сдвиг по ключу
            decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))  #Расшифровываем символ
            plaintext.append(decrypted_char)  #Добавляем расшифрованный символ в список
            keyword_index += 1  #Переходим к следующему символу ключа
        else:
            plaintext.append(char)  #Если символ не алфавитный, добавляем его без изменений

    return ''.join(plaintext)  #Возвращаем расшифрованный текст в виде строки


# Примеры использования
if __name__ == "__main__":  #Проверяем, запущен ли скрипт напрямую
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))  #Шифруем текст
    print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))  #Расшифровываем текст
