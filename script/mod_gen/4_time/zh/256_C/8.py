def f(h1, h2, h3, w1, w2, w3):
    h1, h2, h3 = sorted([h1, h2, h3])
    w1, w2, w3 = sorted([w1, w2, w3])
    if h1 * w1 + h2 * w2 + h3 * w3 != h1 * w2 + h2 * w3 + h3 * w1:
        return 0
    if h1 * w1 + h2 * w2 + h3 * w3 != h1 * w3 + h2 * w1 + h3 * w2:
        return 0
    return 1
h1, h2, h3, w1, w2, w3 = map(int, input().split())
print(f(h1, h2, h3, w1, w2, w3))
