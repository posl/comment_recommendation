def base_minus2(n):
    if n == 0:
        return '0'
    res = ''
    while n != 0:
        res = str(n % (-2)) + res
        n = n // (-2)
    return res
