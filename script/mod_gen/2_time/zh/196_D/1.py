def f(h, w, a, b):
    # h, w: height and width of the room
    # a: number of 2x1 tatami mats
    # b: number of 1x1 tatami mats
    if h == 0 and w == 0:
        return 1
    if h < 0 or w < 0:
        return 0
    if a < 0 or b < 0:
        return 0
    if h < w:
        h, w = w, h
    if (h, w, a, b) not in memo:
        memo[(h, w, a, b)] = f(h - 1, w, a - 2, b) + \
                            f(h - 1, w - 1, a - 1, b - 1) + \
                            f(h - 1, w - 2, a, b - 2)
    return memo[(h, w, a, b)]
memo = {}
h, w, a, b = map(int, input().split())
print(f(h, w, a, b))
