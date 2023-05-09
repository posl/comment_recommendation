def calc_d(x):
    d = 0
    for i in x:
        if int(i) > d:
            d = int(i)
    return d
