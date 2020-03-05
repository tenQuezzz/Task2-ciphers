import prev.Caesar as caesar
import prev.vigenere as vig
import prev.affine as aff
from helper import find_mod_inverse


def cbc_encrypt(data, iv, key, type, thr=0):
    encrypted = []
    iv = iv
    encrypted += data[:thr]
    for ch in data[thr:]:
        xored = ch ^ iv
        if type == 'caesar':
            encr_ch = caesar.encrypt(xored, key)
        elif type == 'vigenere':
            encr_ch = vig.encrypt([xored], key)
        elif type == 'affine':
            encr_ch = aff.encrypt(xored, key['a'], key['b'])
        iv = encr_ch
        encrypted.append(encr_ch)
    return encrypted


def cbc_decrypt(cipher_data, iv, key, type, thr=0):
    decrypted = []
    iv = iv
    decrypted += cipher_data[:thr]
    for i in range(thr, len(cipher_data)):
        if type == 'caesar':
            decr_ch = caesar.decrypt(cipher_data[i], key)
        elif type == 'vigenere':
            decr_ch = vig.decrypt_chunk(cipher_data[i], key[i % len(key)])
        elif type == 'affine':
            decr_ch = aff.decrypt(
                cipher_data[i], find_mod_inverse(key['a'], 256), key['b'])
        decrypted.append(iv ^ decr_ch)
        iv = cipher_data[i]
    return decrypted
