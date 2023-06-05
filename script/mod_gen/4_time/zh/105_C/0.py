def to_base2(n):
    if n == 0:
        return '0'
    s = ''
    while n != 0:
        if n % 2 == 0:
            s = '0' + s
        else:
            s = '1' + s
            n -= 1
        n /= -2
    return s

if __name__ == '__main__':
    to_base2()