def calc(a, b):
    s = b - a
    x = int((2 * s + 0.25) ** 0.5 - 0.5)
    if x * (x + 1) < s:
        x += 1
    return x
