def convert(n):
    if n == 0:
        return '0'
    s = ''
    while n != 0:
        if n % 2 == 0:
            s = '0' + s
            n = n // (-2)
        else:
            s = '1' + s
            n = (n - 1) // (-2)
    return s
