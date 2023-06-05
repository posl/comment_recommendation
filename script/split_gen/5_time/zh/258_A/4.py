def f(k):
    m = k % 60
    h = k // 60 + 21
    if h > 23:
        h -= 24
    return '{:02d}:{:02d}'.format(h, m)
