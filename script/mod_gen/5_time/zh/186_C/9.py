def check(num, base):
    while num > 0:
        if num % base == 7:
            return False
        num /= base
    return True

if __name__ == '__main__':
    check()