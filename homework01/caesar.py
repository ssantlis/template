def encrypt_caesar(plaintext, shift=3):
    """
    Encrypt the plaintext using Caesar cipher with a specified shift.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""


    for char in plaintext:
        if char.isalpha():  #Проверяем, что символ - буква
            #Вычисляем базовый код для 'A' или 'a'
            base = ord('A') if char.isupper() else ord('a')
            #Шифрование с учетом сдвига
            new_char = chr((ord(char) - base + shift) % 26 + base)
            #ord() для получения числового кода символа и chr() для преобразования обратно в символ.
            ciphertext += new_char
        else:
            ciphertext += char  #Не буквы (иные символы) записываются без изменений

    return ciphertext


def decrypt_caesar(ciphertext, shift=3):
    """
    Decrypt the ciphertext using Caesar cipher with a specified shift.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():  #Проверяем, что символ - буква
            #Вычислить базовый код для 'A' или 'a'
            base = ord('A') if char.isupper() else ord('a')
            #Дешифрование с учетом сдвига
            new_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += new_char
        else:
            plaintext += char  #Не буквы остаются без изменений

    return plaintext


encrypted = encrypt_caesar("Hello, World!", shift=5)
print(encrypted)  #Консоль выводит зашифрованный текст

decrypted = decrypt_caesar(encrypted, shift=5)
print(decrypted)  #Консоль вывходит исходный текст


