def base_minus2(n):
    if n == 0:
        return '0'
    s = ''
    while n:
        s += str(n % -2)
        n = (n - n % -2) // -2
    return s[::-1]
