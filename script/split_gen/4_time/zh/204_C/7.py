def calc(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return calc(a, b - 1) + calc(a, b - 2) + calc(a, b - 3)
