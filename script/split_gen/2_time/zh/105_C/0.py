def base2(num):
    if num == 0:
        return 0
    res = ""
    while num != 0:
        if num % (-2) == 0:
            res = "0" + res
        else:
            res = "1" + res
            num -= 1
        num //= -2
    return res
