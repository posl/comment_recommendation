def get_digits(num, base):
    digits = 0
    while num > 0:
        digits += 1
        num //= base
    return digits

if __name__ == '__main__':
    get_digits()