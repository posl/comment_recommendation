def toMinus2(num):
    if num == 0:
        return '0'
    s = ''
    while num != 0:
        if num % 2 == 0:
            s = '0' + s
        else:
            s = '1' + s
            num -= 1
        num //= -2
    return s
N = int(input())
print(toMinus2(N))
