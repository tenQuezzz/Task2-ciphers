def encrypt(ch, key):
    c = (ch + key) % 256
    return c


def decrypt(ch, key):
    c = (ch - key) % 256
    return c


def encrypt_data(data, key, thr=0):
    encrypted = []
    encrypted += data[:thr]
    for value in data[thr:]:
        encrypted.append(encrypt(value, key))
    return encrypted


def decrypt_data(data, key, thr=0):
    decrypted = []
    decrypted += data[:thr]
    for value in data[thr:]:
        decrypted.append(decrypt(value, key))
    return decrypted
