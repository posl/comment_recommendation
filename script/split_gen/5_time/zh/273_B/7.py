def roundUp(x, k):
    if k == 0:
        return x
    y = x
    if x % (10 ** k) >= 5 * (10 ** (k - 1)):
        y = x + 10 ** k - x % (10 ** k)
    else:
        y = x - x % (10 ** k)
    return y
