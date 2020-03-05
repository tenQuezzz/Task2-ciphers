import prev.Caesar as caesar
import prev.vigenere as vig
import prev.affine as aff


def ofb_decrypt(cipher_data, iv, key, type, thr=0):
    decrypted = []
    decrypted += cipher_data[:thr]
    iv = iv
    for i in range(thr, len(cipher_data)):
        if type == 'caesar':
            decr_ch = caesar.encrypt(iv, key)
        elif type == 'vigenere':
            decr_ch = vig.encrypt_chunk(iv, key[i % len(key)])
        elif type == 'affine':
            decr_ch = aff.encrypt(iv, key['a'], key['b'])
        iv = decr_ch
        decr_ch = cipher_data[i] ^ decr_ch
        decrypted.append(decr_ch)
    return decrypted


def ofb_encrypt(data, iv, key, type, thr=0):
    encrypted = []
    encrypted += data[:thr]
    iv = iv
    for ch in data[thr:]:
        if type == 'caesar':
            encr_ch = caesar.encrypt(iv, key)
        elif type == 'vigenere':
            encr_ch = vig.encrypt_chunk(iv, key)
        elif type == 'affine':
            encr_ch = aff.encrypt(iv, key['a'], key['b'])
        iv = encr_ch
        encr_ch = encr_ch ^ ch
        encrypted.append(encr_ch)
    return encrypted
