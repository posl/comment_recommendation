def get_combination(a, b):
    if a == 0 or b == 0:
        return 1
    else:
        return get_combination(a - 1, b) + get_combination(a, b - 1)
