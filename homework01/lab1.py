def encrypt_caesar(plaintext, shift):
    alph_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_low = alph_cap.lower()
    code = ''
    for i in plaintext:
        if i in alph_cap:
            symb = ord(i) + shift % 26
            if symb > 90:
                symb -= 26
            code += chr(symb)
        elif i in alph_low:
            symb = ord(i) + shift % 26
            if symb > 122:
                symb -= 26
            code += chr(symb)
        else:
            code += i
    return code

def decrypt_caesar(ciphertext, shift):
    alph_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_low = alph_cap.lower()
    code = ''
    for i in ciphertext:
        if i in alph_cap:
            symb = ord(i) - shift % 26
            if symb < 65:
                symb += 26
            code += chr(symb)
        elif i in alph_low:
            symb = ord(i) - shift % 26
            if symb < 97:
                symb += 26
            code += chr(symb)
        else:
            code += i
    return code

s = input()
n = int(input())
coded = encrypt_caesar(s, n)
decoded = decrypt_caesar(coded, n)
print(coded, decoded)