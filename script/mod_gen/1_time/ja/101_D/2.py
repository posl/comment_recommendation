def sum_digits(n):
    """nの各桁の和を返す"""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    sum_digits()