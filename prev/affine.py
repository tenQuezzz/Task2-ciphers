def encrypt(ch, a, b):
    return (ch * a + b) % 256


def decrypt(ch, a_inv, b):
    return a_inv * (ch - b) % 256


def encrypt_data(data, a, b):
    cipher_data = []
    for ch in data:
        cipher_data.append(encrypt_data(ch, a, b))
    return cipher_data


def decrypt_data(data, a_inv, b):
    decrypted_data = []
    for ch in data:
        decrypted_data.append(decrypt(ch, a_inv, b))
    return decrypted_data
