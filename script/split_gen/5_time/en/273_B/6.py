def round_x(x, k):
    for i in range(k):
        if x % 10 != 0:
            x += 10 - (x % 10)
        else:
            x //= 10
    return x
