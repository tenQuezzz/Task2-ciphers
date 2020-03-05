from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write
from detectEnglish import isEnglish
from itertools import permutations

alphabet_size = 256


def encrypt(data, k, border=0):
    key = [ord(ch) for ch in k]
    key_length = len(key)
    encrypted = []
    i = 0
    encrypted += data[:border]
    for chunk in data[border:]:
        encrypted_chunk = (chunk + key[i % key_length]) % alphabet_size
        encrypted.append(encrypted_chunk)
        i += 1
    return encrypted


def decrypt(data, k, border=0):
    key = [ord(ch) for ch in k]
    key_length = len(key)
    i = 0
    decrypted = []
    decrypted += data[:border]
    for chunk in data[border:]:
        decrypted_chunk = (chunk - key[i % key_length]) % alphabet_size
        decrypted.append(decrypted_chunk)
        i += 1
    return decrypted

def decrypt_chunk(data, key):
    result = (data - key) % alphabet_size
    return result

def encrypt_chunk(data, key):
    result = (data + key) % alphabet_size
    return result


def task8():
    encrypted_data = read('./imgs/im6_vigener_c_all.bmp')
    decrypted_data = decrypt(encrypted_data, 'magistr')
    write('./imgs/task8_decrypted.bmp', decrypted_data)


def task8_plus():
    bmp_data = read('task8_decrypted.bmp')
    encrypted_data = encrypt(bmp_data, 'magistr', border=50)
    print(bmp_data[:50] == encrypted_data[:50])
    write('./imgs/task8_encr50.bmp', encrypted_data)


def longest_word(words):
    max_len = 0
    res = None
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            res = word
    if res:
        return res
    return None


def task9():
    encrypted_data = read('./text_files/text4_vigener_c_all.txt')
    possible_word = ' ' * 10
    data = [ord(' ')] * len(possible_word)
    found_word = ''
    english_words = []
    for i in range(len(encrypted_data) - len(possible_word)):
        for j in range(len(possible_word)):
            ch = (encrypted_data[i + j] - data[j]) % alphabet_size
            found_word += chr(ch)
            if isEnglish(found_word):
                english_words.append(found_word)
        possible_key = longest_word(english_words)
        if possible_key:
            return possible_key
        found_word = ''
    return None


def guess_keys(encrypted_data, known_bytes):
    keys = []
    for i in range(len(encrypted_data) - len(known_bytes)):
        text = ''
        for j in range(len(known_bytes)):
            ch = (encrypted_data[i + j] - known_bytes[j]) % alphabet_size
            text += chr(ch)
            if isEnglish(text):
                keys.append(text)
        print(text)
    return keys


def task10():
    encrypted_data = read('./text_files/text4_vigener_c_all.txt')
    known_data = [ord(ch) for ch in 'housewives']
    for i in range(len(encrypted_data) - len(known_data)):
        text = ''
        for j in range(len(known_data)):
            ch = (encrypted_data[i + j] - known_data[j]) % alphabet_size
            text += chr(ch)
            if isEnglish(text):
                print(f'**** POSSIBLE ENGLISH: {text} ******')
        print(text)


def task11():
    encrypted_data = read('./text_files/text1_vigener_c.txt')
    # known_data = [ord(ch) for ch in 'it therefore']
    # keys = guess_keys(encrypted_data, known_data)

    key = 'KEYBOARD'
    decrypted_data = decrypt(encrypted_data, key)
    print(''.join(chr(ch) for ch in decrypted_data))


def task12():
    perms = permutations([0, 1, 2, 3, 4, 5])
    for p in perms:
        print(p)


if __name__ == '__main__':
    pass
