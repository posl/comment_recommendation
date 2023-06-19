def washHair(v, a, b, c):
    if v < a:
        return 'F'
    elif v < a + b:
        return 'M'
    else:
        return 'T'
