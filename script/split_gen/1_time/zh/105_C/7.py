def base_minus2(n):
    if n == 0:
        return '0'
    result = ''
    while n != 0:
        if n % (-2) == 0:
            result += '0'
            n = n / (-2)
        else:
            result += '1'
            n = (n - 1) / (-2)
    return result[::-1]
