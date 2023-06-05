def get_exp(x, y, a, b):
    exp = 0
    str = x
    while str < y:
        if str * a < str + b:
            str *= a
        else:
            str += b
        exp += 1
    return exp

if __name__ == '__main__':
    get_exp()