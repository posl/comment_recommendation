def round_to_10(x,k):
    for i in range(k):
        if x % 10 != 0:
            x += 1
        else:
            x = x // 10
    return x
