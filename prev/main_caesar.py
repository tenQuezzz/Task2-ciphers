import Caesar
from detectEnglish import isEnglish
from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write
import substitution


def task1():
    encrypted_data = read('./text_files/t3_caesar_c_all.txt')
    for key in range(256):
        decrypted = Caesar.decrypt_data(encrypted_data[:25], key)
        txt = ''.join(chr(ch) for ch in decrypted)
        if isEnglish(txt):
            break
    decrypted_data = Caesar.decrypt_data(encrypted_data, key)
    write('./text_files/task1_decrypted.txt', decrypted_data)


def task2():
    encrypted_img_data = read('./imgs/c4_caesar_c_all.bmp')
    for key in range(256):
        decrypted = Caesar.decrypt_data(encrypted_img_data[:2], key)
        if decrypted == [66, 77]:
            print(f'Key is {key}')
            break
    decrypted_bmp = Caesar.decrypt_data(encrypted_img_data, key)
    write('./imgs/task2_decrypted_bmp.BMP', decrypted_bmp)


def task3():
    encrypted_data = read('c3_subst_c_all.png')
    decrypted_data = substitution.decrypt(encrypted_data)
    write('./imgs/task3_decrypted.png', decrypted_data)


if __name__ == '__main__':
    pass
