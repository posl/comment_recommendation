def get_max_weight(x, y, w, s):
    if len(x) == 0:
        return s
    else:
        return get_max_weight(x[1:], y[1:], w[1:], max(s, w[0], get_max_weight(x[1:], y[1:], w[1:], s)))
