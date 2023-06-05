def cal_max_exp(x, y, a, b):
    exp = 0
    while True:
        if (x * a) > (x + b):
            x *= a
            exp += 1
            if x >= y:
                break
        else:
            x += b
            exp += 1
            if x >= y:
                break
    return exp
