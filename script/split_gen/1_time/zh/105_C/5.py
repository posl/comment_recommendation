def radix2(num):
    if num == 0:
        return '0'
    res = ''
    while num != 0:
        num, mod = divmod(num, -2)
        if mod == -1:
            mod = 1
            num += 1
        res = str(mod) + res
    return res
