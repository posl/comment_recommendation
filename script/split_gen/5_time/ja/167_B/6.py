def max_sum(a, b, c, k):
    if a >= k:
        return k
    elif a + b >= k:
        return a
    else:
        return a - (k - a - b)
