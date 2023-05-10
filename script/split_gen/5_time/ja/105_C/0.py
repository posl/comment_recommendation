def get2n(n):
    if n == 0:
        return '0'
    result = ''
    while n != 0:
        if n % 2 == 0:
            result = '0' + result
            n /= -2
        else:
            result = '1' + result
            n = (n - 1) / -2
    return result
