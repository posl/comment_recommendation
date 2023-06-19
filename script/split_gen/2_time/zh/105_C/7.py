def base_2(n):
    if n == 0:
        return '0'
    res = ''
    while n:
        res = str(n % -2) + res
        n = n // -2
    return res
