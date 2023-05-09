def comma_num(n):
    if n < 1000:
        return 0
    elif n < 1000000:
        return n - 999
    elif n < 1000000000:
        return 999000 + (n - 999999)
    elif n < 1000000000000:
        return 999000000 + (n - 999999999)
    elif n < 1000000000000000:
        return 999000000000 + (n - 999999999999)
    else:
        return 999000000000000 + (n - 999999999999999)
n = int(input())
print(comma_num(n))
