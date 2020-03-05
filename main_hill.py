from helper import gcd, find_mod_inverse
import numpy as np
from math import floor
from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write


ALPHABET_SIZE = 256


def find_inverse_key(key):
    det = abs(int(np.linalg.det(key).round()))
    if gcd(det, ALPHABET_SIZE) == 1:
        inverse_det = find_mod_inverse(det, ALPHABET_SIZE)
        if inverse_det is None:
            return None
        res = (np.array([[key[1, 1], -key[0, 1]], [-key[1, 0],
                                                   key[0, 0]]]) * inverse_det) % ALPHABET_SIZE
        return res
    return None

def decode(filename, output_name, key):
    encrypted_data = read(filename)
    inv_key = find_inverse_key(key)
    decrypted_data = []
    for i in range(0, len(encrypted_data), 2):
        d = np.array([encrypted_data[i], encrypted_data[i+1]])
        decrypted = np.matmul(inv_key, d) % ALPHABET_SIZE
        decrypted_data += list(decrypted)
    write(output_name, data=decrypted_data)

def task1():
    filename = 'images/im3_hill_c_all.bmp'
    key = np.array([[189, 58], [21, 151]])
    decode(filename, 'decrypted_images/decrypted_task1.bmp', key)


def task2():
    filename = 'images/b4_hill_c_all.png'
    encrypted_data = read(filename)
    png_bytes = np.array([[137, 78], [80, 71]])
    enc_bytes = np.array([[23, 239], [3, 52]])
    inv_png_bytes = find_inverse_key(png_bytes)
    key = np.matmul(enc_bytes, inv_png_bytes) % ALPHABET_SIZE
    decode(filename, 'decrypted_images/task2.png', key)

def task3():
    filename = 'text/text2_hill_c_all.txt'
    word_bytes = np.array([[87, 111], [104, 115]])
    enc_bytes = np.array([[15, 93], [169, 158]])
    inv_key = find_inverse_key(word_bytes)
    key = np.matmul(enc_bytes, inv_key) % ALPHABET_SIZE
    print(f'key: {key}')
    decode(filename, 'decrypted_text/task2.txt', key)


if __name__ == '__main__':
    pass
    # task1()
    # task2()
    # task3()
