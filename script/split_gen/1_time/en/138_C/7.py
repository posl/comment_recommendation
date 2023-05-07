def max_value(N, v):
    v.sort()
    while len(v) > 1:
        v[0] = (v[0] + v[1]) / 2.0
        del v[1]
        v.sort()
    return v[0]
