import random
import math
import typing as tp
def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    # PUT YOUR CODE HERE
    pass

    if n <= 1:
        return False  #Числа меньше или равные 1 не являются простыми
    for i in range(2, int(n ** 0.5) + 1):  #Проверяем делимость от 2 до корня из n
        if n % i == 0:  #Если n делится на i без остатка, значит, это не простое число
            return False
    return True  #Если не найдено делителей, n - простое число

def gcd(a: int, b: int) -> int:
    """
    Находит наибольший общий делитель (НОД) двух чисел.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b != 0:  #Пока b не равно 0
        a, b = b, a % b  #Используем алгоритм Евклида
    return a  #Возвращаем НОД

def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Находит обратное по модулю число d для e по модулю phi.
    >>> multiplicative_inverse(7, 40)
    23
    """
    m0, y, x = phi, 0, 1  #m0 хранит значение phi, y и x - временные переменные
    if phi == 1:
        return 0  #Если phi = 1, то обратного элемента не существует
    while e > 1:  #Пока e больше 1
        #q – частное, t – остаток
        q = e // phi  #Делим e на phi
        t = phi  #Сохраняем текущее значение phi
        phi = e % phi  #Находим остаток от деления
        e = t  #Обновляем e
        t = y  #Сохраняем старое значение y
        y = x - q * y  #Обновляем y
        x = t  #Обновляем x
    #Убедимся, что x положительное
    if x < 0:
        x += m0  #Если x отрицательное, добавляем m0 для получения положительного значения
    return x  # Возвращаем обратное число

def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    """
    Шифрует сообщение с использованием публичного ключа.
    """
    key, n = pk  #Извлекаем ключ и n из публичного ключа
    cipher = [(ord(char) ** key) % n for char in plaintext]  #Шифруем каждую букву сообщения
    return cipher  #Возвращаем зашифрованное сообщение в виде списка целых чисел

def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """
    Дешифрует сообщение с использованием приватного ключа.
    """
    key, n = pk  #Извлекаем ключ и n из приватного ключа
    plain = [chr((char ** key) % n) for char in ciphertext]  #Дешифруем каждое число в исходное сообщение
    return "".join(plain)  #Преобразуем список символов обратно в строку и возвращаем

if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(" ".join(map(str, encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))


