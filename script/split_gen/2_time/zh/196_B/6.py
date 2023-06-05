def max_x_y(a, b, c, d):
    x = a
    y = c
    if (a + c) < (a + d):
        y = d
    if (a + c) < (b + c):
        x = b
    return x - y
