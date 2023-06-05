def baseKTo10(baseK, num):
    base10 = 0
    for i in range(len(num)):
        base10 += int(num[i]) * (baseK ** (len(num) - i - 1))
    return base10
