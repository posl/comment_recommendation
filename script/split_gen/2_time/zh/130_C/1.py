def solve(w, h, x, y):
    s = w * h / 2
    if (x == w / 2 and y == h / 2):
        return [s, 1]
    else:
        return [s, 0]
