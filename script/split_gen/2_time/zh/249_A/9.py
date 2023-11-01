def who_is_in_front(a, b, c, d, e, f, x):
    takahashi = 0
    aoki = 0
    while x > 0:
        if takahashi == aoki:
            takahashi += a
            aoki += d
        elif takahashi > aoki:
            aoki += e
        else:
            takahashi += b
        x -= 1
        if x > 0:
            x -= c
        if x > 0:
