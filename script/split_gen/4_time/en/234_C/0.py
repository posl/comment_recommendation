def base2(n):
    if n == 0:
        return '0'
    else:
        s = ''
        while n > 0:
            s = str(n % 2) + s
            n = n // 2
        return s
