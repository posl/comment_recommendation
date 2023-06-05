def pow(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        return pow(a, b/2) * pow(a, b/2)
    else:
        return pow(a, b/2) * pow(a, b/2) * a
