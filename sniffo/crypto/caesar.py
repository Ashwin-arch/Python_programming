# crypto/caesar.py

CHARSET = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'abcdefghijklmnopqrstuvwxyz'
    '0123456789'
    '!@#$%^&*()-_=+[]{}|;:<>,.?/~`'
)

def encrypt(text, shift):
    encrypted = ''
    for char in text:
        if char in CHARSET:
            index = CHARSET.index(char)
            new_index = (index + shift) % len(CHARSET)
            encrypted += CHARSET[new_index]
        else:
            encrypted += char  # Keep unsupported characters unchanged
    return encrypted

def decrypt(text, shift):
    decrypted = ''
    for char in text:
        if char in CHARSET:
            index = CHARSET.index(char)
            new_index = (index - shift) % len(CHARSET)
            decrypted += CHARSET[new_index]
        else:
            decrypted += char
    return decrypted
