def round_off(x, k):
    for i in range(1, k+1):
        x = round(x, -i)
    return x
