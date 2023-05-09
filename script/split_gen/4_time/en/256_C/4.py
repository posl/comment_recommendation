def solve(h1, h2, h3, w1, w2, w3):
    if h1 + h2 + h3 != w1 + w2 + w3:
        return 0
    if h1 > w1 or h2 > w2 or h3 > w3:
        return 0
    if h1 + h2 > w1 + w2:
        return 0
    if h2 + h3 > w2 + w3:
        return 0
    if h3 + h1 > w3 + w1:
        return 0
    if h1 + h2 + h3 == w1 + w2 + w3:
        return 1
