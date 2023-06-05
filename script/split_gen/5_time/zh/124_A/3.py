def get_max_coin(a, b):
    if a >= b:
        return a + a - 1
    else:
        return b + b - 1
