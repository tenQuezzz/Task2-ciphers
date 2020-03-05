from cbc import cbc_encrypt, cbc_decrypt
from ofb import ofb_decrypt, ofb_encrypt
from cfb import cfb_encrypt, cfb_decrypt
from ctr import ctr_encrypt, ctr_decrypt
from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write
import prev.Caesar as caesar
from helper import gcd, find_mod_inverse


def task4():
    plaintext = [1, 2, 3, 4]
    iv = 1
    key = 3
    return cbc_encrypt(plaintext, iv, key, type='caesar')


def task5():
    filename = 'images/z1_caesar_cbc_c_all.bmp'
    encrypted_data = read(filename)
    key = 223
    iv = 59
    decrypted = cbc_decrypt(encrypted_data, iv, key, type='caesar')
    write('decrypted_images/task5.bmp', decrypted)

    # encryption of task5.bmp using CBC except first 50 bytes
    data = read('decrypted_images/task5.bmp')
    encrypted = cbc_encrypt(data, iv, key, type='caesar', thr=50)
    write('decrypted_images/task5_cbs_50.bmp', encrypted)
    # encryption of task5.bmp using ECB except first 50 bytes
    encrypted = caesar.encrypt_data(data, key, thr=50)
    write('decrypted_images/task5_ecb_50.bmp', encrypted)


def task6():
    filename = 'images/im8_caesar_ofb_c_all.bmp'
    key = 56
    iv = 9
    cipher_data = read(filename)
    decrypted = ofb_decrypt(cipher_data, iv, key, type='caesar')
    write('decrypted_images/task6.bmp', decrypted)
    # ofb encryption
    data = read('decrypted_images/task6.bmp')
    encrypted = ofb_encrypt(data, iv, key, type='caesar', thr=50)
    write('decrypted_images/task6_ofb_50.bmp', encrypted)
    # # ecb encryption
    encrypted = caesar.encrypt_data(data, key, thr=50)
    write('decrypted_images/task6_ecb_50.bmp', encrypted)


def task7():
    filename = 'images/z2_caesar_cfb_c_all.bmp'
    cipher_data = read(filename)
    iv = 9
    key = 174
    decrypted = cfb_decrypt(cipher_data, iv, key, type='caesar')
    write('decrypted_images/task7.bmp', decrypted)


def task8():
    filename = 'images/z3_caesar_ctr_c_all.bmp'
    cipher_data = read(filename)
    key = 223
    iv = 78
    decrypted = ctr_decrypt(cipher_data, iv, key, 'caesar')
    write('decrypted_images/task8.bmp', decrypted)
    # encr ctr
    data = read('decrypted_images/task8.bmp')
    encrypted = ctr_encrypt(data, iv, key, 'caesar', thr=50)
    write('decrypted_images/task8_ctr_50.bmp', encrypted)
    # encr ecb
    encrypted = caesar.encrypt_data(data, key, thr=50)
    write('decrypted_images/task8_ecb_50.bmp', encrypted)


def task9():
    data = read('decrypted_images/task5.bmp')
    key = 223
    iv = 78
    encrypted_data_ecb = caesar.encrypt_data(data, key, thr=50)
    write('task9_ecb.bmp', encrypted_data_ecb)
    encrypted_data_ofb = ofb_encrypt(data, iv, key, type='caesar', thr=50)
    write('task9_ofb.bmp', encrypted_data_ofb)
    encrypted_data_cfb = cfb_encrypt(data, iv, key, type='caesar', thr=50)
    write('task9_cfb.bmp', encrypted_data_cfb)
    encrypted_data_cbc = cbc_encrypt(data, iv, key, type='caesar', thr=50)
    write('task9_cbc.bmp', encrypted_data_cbc)
    encrypted_data_ctr = ctr_encrypt(data, iv, key, type='caesar', thr=50)
    write('task9_ctr.bmp', encrypted_data_ctr)


def task10():
    filename = 'images/z5_vigener_cbc_c_all.bmp'
    cipher_data = read(filename)
    key = [ord(ch) for ch in 'MODELING']
    iv = 67
    decrypted = cbc_decrypt(cipher_data, iv, key, type='vigenere')
    write('decrypted_images/task10.bmp', decrypted)


def task11():
    filename = 'images/im4_vigener_ofb_c_all.bmp'
    cipher_data = read(filename)
    key = [ord(ch) for ch in 'MODULATOR']
    iv = 217
    res = ofb_decrypt(cipher_data, iv, key, type='vigenere')
    write('decrypted_images/task11.bmp', res)


def task12():
    filename = 'images/im5_vigener_cfb_c_all.bmp'
    cipher_data = read(filename)
    key = [ord(ch) for ch in 'MONARCH']
    iv = 172
    res = cfb_decrypt(cipher_data, iv, key, type='vigenere')
    write('decrypted_images/task12.bmp', res)


def task13():
    filename = 'images/z6_vigener_ctr_c_all.bmp'
    cipher_data = read(filename)
    key = [ord(ch) for ch in 'MONOLITH']
    iv = 167
    res = ctr_decrypt(cipher_data, iv, key, 'vigenere')
    write('decrypted_images/task13.bmp', res)


def task14():
    filename = 'images/im15_affine_cbc_c_all.bmp'
    cipher_data = read(filename)
    key = {'a': 129, 'b': 107}
    iv = 243
    decrypted = cbc_decrypt(cipher_data, iv, key, type='affine')
    write('decrypted_images/task14.bmp', decrypted)


def task15():
    filename = 'images/im16_affine_ofb_c_all.bmp'
    cipher_data = read(filename)
    key = {'a': 233, 'b': 216}
    iv = 141
    decrypted = ofb_decrypt(cipher_data, iv, key, type='affine')
    write('decrypted_images/task15.bmp', decrypted)


def task16():
    filename = 'images/im17_affine_сfb_c_all.bmp'
    cipher_data = read(filename)
    key = {'a': 117, 'b': 239}
    iv = 19
    decrypted = cfb_decrypt(cipher_data, iv, key, type='affine')
    write('decrypted_images/task16.bmp', decrypted)


def task17():
    filename = 'images/z4_affine_сtr_c_all.bmp'
    cipher_data = read(filename)
    key = {'a': 61, 'b': 18}
    iv = 92
    decrypted = ctr_decrypt(cipher_data, iv, key, 'affine')
    write('decrypted_images/task17.bmp', decrypted)


if __name__ == '__main__':
    print(task4())
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    # task11()
    # task12()
    # task13()
    # task14()
    # task15()
    # task16()
    # task17()
