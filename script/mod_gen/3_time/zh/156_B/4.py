def get_digits(num):
    digits = 0
    while num:
        num //= 10
        digits += 1
    return digits

if __name__ == '__main__':
    get_digits()