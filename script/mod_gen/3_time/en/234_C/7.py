def get_digit(K, base):
    digit = 0
    while K > 0:
        digit += 1
        K //= base
    return digit

if __name__ == '__main__':
    get_digit()