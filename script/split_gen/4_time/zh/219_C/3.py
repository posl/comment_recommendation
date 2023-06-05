def lex_cmp(x, y, order):
    for i in range(0, min(len(x), len(y))):
        if order.index(x[i]) < order.index(y[i]):
            return -1
        elif order.index(x[i]) > order.index(y[i]):
            return 1
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1
    else:
        return 0
