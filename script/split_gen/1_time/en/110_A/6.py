def max_allowance(a, b, c):
    return max(a + b + c, a * (b + c), (a + b) * c, a * b * c)
