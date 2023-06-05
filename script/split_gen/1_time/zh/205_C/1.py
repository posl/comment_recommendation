def pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return pow(a, b // 2) * pow(a, b // 2)
    else:
        return pow(a, b // 2) * pow(a, b // 2) * a
