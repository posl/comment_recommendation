def get_digit(num):
    digit = 0
    while num > 0:
        num //= 10
        digit += 1
    return digit

if __name__ == '__main__':
    get_digit()