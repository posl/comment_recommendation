def get_digit(n):
    digit = 0
    while n > 0:
        n = n // 10
        digit += 1
    return digit

if __name__ == '__main__':
    get_digit()