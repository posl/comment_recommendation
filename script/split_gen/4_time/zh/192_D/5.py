def get_num(x, m):
    d = max(x)
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    else:
        if int(x[0]) < d:
            return 0
        else:
            return get_num(x[1:], m) + get_num(x[1:], m - int(x[0]))
