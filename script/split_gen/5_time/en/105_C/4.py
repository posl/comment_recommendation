def base_minus_2(n):
    if n == 0:
        return '0'
    s = ''
    while n != 0:
        if n % 2 == 0:
            s = '0' + s
            n //= -2
        else:
            s = '1' + s
            n = (n - 1) // -2
    return s
n = int(input())
print(base_minus_2(n))
