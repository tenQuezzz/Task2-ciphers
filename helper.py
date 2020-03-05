from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write


def frequency_analysis(message):
    frequencies = dict({})
    for ch in message:
        if ch in frequencies:
            frequencies[ch] += 1
        else:
            frequencies[ch] = 1
    return frequencies


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


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def read_file(filename):
    data = read(filename)
    return data


if __name__ == '__main__':
    print(find_mod_inverse(7, 26))
    # print(gcd(7, 26))
