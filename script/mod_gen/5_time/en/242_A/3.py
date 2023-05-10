def calc_probability(a, b, c, x):
    if x <= a:
        return 1
    elif a < x <= b:
        return c / (b - a)
    else:
        return 0

if __name__ == '__main__':
    calc_probability()