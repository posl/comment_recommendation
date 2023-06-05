def base2(num):
    if num == 0:
        return '0'
    ans = ''
    while num != 0:
        if num % 2 == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            num -= 1
        num = num // (-2)
    return ans
