from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write
from detectEnglish import isEnglish
from itertools import permutations


def decode_block(block, key):
    if len(block) == len(key):
        output = [0] * len(block)
        for i in range(len(block)):
            output[i] = block[key[i]]
        return output
    return ""


def decrypt(data, key, block_size):
    text = ''
    for i in range(0, len(data) - block_size - 1, block_size):
        block = data[i:i + block_size]
        decrypted_block = decode_block(block, key)
        txt = ''.join(chr(ch) for ch in decrypted_block)
        text += txt
    return text


def task12():
    encrypted_data = read('./text_files/text2_permutation_c.txt')
    for key in permutations([0, 1, 2, 3, 4, 5]):
        decrypted_text = decrypt(encrypted_data, key, len(key))
        if isEnglish(decrypted_text):
            print(f"Possible key: {key}")
            print(f'Message part: {decrypted_text}')


if __name__ == '__main__':
    task12()
