def solve(a, b, c, k):
    if k <= a:
        return k
    if k <= a + b:
        return a
    return a - (k - a - b)
