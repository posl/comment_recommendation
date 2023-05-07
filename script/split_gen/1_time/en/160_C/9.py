def getDistance(a, b, k):
    if a > b:
        a, b = b, a
    return min(b - a, a + k - b)
