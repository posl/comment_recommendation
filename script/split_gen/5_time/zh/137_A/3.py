def max_num(a, b):
    if a + b > a - b:
        if a + b > a * b:
            return a + b
        else:
            return a * b
    else:
        if a - b > a * b:
            return a - b
        else:
            return a * b
