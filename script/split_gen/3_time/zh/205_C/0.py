def pow(a, b):
    if a < 0 and b % 2 == 0:
        return -a**b
    else:
        return a**b
