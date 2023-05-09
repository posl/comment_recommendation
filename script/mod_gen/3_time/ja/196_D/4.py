def calc_combination(a, b):
    if b == 0 or a == b:
        return 1
    else:
        return calc_combination(a - 1, b - 1) + calc_combination(a - 1, b)

if __name__ == '__main__':
    calc_combination()