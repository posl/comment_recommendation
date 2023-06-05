def base2(num):
    if num == 0:
        return '0'
    result = ''
    while num != 0:
        if num % 2 == 0:
            result = '0' + result
        else:
            result = '1' + result
            num -= 1
        num //= -2
    return result
num = int(input())
print(base2(num))
