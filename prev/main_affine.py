from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write
from detectEnglish import isEnglish
import affine


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def find_mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def task4():
    print(find_mod_inverse(550, 1759) == 355)


def task5():
    a = 19
    b = 236
    a_inv = find_mod_inverse(a, 256)
    encrypted_bmp_data = read('./imgs/ff2_affine_c_all.bmp')
    decrypted_bmp_data = affine.decrypt_data(encrypted_bmp_data, a_inv, b)
    write('./imgs/task5_decrypted.BMP', decrypted_bmp_data)


def task6():
    encrypted_data = read('./text_files/text10_affine_c_all.txt')
    count = 0
    keys = None
    for a in range(256):
        if keys:
            break
        for b in range(256):
            if gcd(a, 256) == 1:
                a_inv = find_mod_inverse(a, 256)
                if a_inv is None:
                    continue
                count += 1
                decrypted_data = affine.decrypt_data(encrypted_data, a_inv, b)
                txt = ''.join(chr(ch) for ch in decrypted_data)
                if isEnglish(txt):
                    print(f"Keys are: a={a}, b={b}\nAttempts: {count}")
                    keys = [a, b]
                    break
    a, b = keys
    decrypted_msg = affine.decrypt_data(
        encrypted_data, find_mod_inverse(a, 256), b)
    txt = ''.join(chr(ch) for ch in decrypted_msg)
    print(f'Original msg:\n{txt}')


def task7():
    encrypted_png_data = read('./imgs/b4_affine_c_all.png')
    count = 0
    keys = None
    for a in range(256):
        if keys:
            break
        for b in range(256):
            if gcd(a, 256) == 1:
                a_inv = find_mod_inverse(a, 256)
                if a_inv is None:
                    continue
                count += 1
                decrypted_data = affine.decrypt_data(
                    encrypted_png_data[:2], a_inv, b)
                if decrypted_data == [137, 80]:
                    print(f'Keys are: a={a}, b={b}, Attempts: {count}')
                    keys = [a, b]
    a, b = keys
    decrypted_png_data = affine.decrypt_data(
        encrypted_png_data, find_mod_inverse(a, 256), b)
    write('./imgs/task7_decrypted.png', decrypted_png_data)


if __name__ == '__main__':
    pass
