def base_minus2(num):
    if num == 0:
        return '0'
    base = ''
    while num != 0:
        if num % (-2) == 0:
            base = '0' + base
            num = num // (-2)
        else:
            base = '1' + base
            num = (num - 1) // (-2)
    return base
num = int(input())
print(base_minus2(num))
