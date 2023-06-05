def round_up(x, k):
    if k == 0:
        return x
    if x == 0:
        return 0
    if x % (10 ** k) == 0:
        return x
    else:
        return round_up(x + 10 ** k - x % (10 ** k), k)
