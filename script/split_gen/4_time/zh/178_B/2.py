def maxProduct(a, b, c, d):
    if a < 0 and b > 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)
    elif a < 0 and b <= 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)
    elif a >= 0 and b > 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)
    elif a >= 0 and b <= 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)
