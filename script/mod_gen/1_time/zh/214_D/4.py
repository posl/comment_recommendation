def get_max_weight(x, y, w, s):
    if len(x) == 0:
        return s
    else:
        return get_max_weight(x[1:], y[1:], w[1:], max(s, w[0], get_max_weight(x[1:], y[1:], w[1:], s)))

if __name__ == '__main__':
    get_max_weight()