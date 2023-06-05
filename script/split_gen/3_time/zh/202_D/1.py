def calc_combination(a, b):
    if a == 0 or b == 0:
        return 1
    return calc_combination(a - 1, b) + calc_combination(a, b - 1)
