def get_digit(x):
    digit = 0
    while x > 0:
        x //= 10
        digit += 1
    return digit

if __name__ == '__main__':
    get_digit()