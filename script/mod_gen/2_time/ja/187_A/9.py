def sum_digit(n):
    """nの各桁の和を返す"""
    return sum([int(i) for i in str(n)])

if __name__ == '__main__':
    sum_digit()