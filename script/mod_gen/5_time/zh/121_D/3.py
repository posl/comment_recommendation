def f(a, b):
    if a == b:
        return a
    if a == 0:
        return 0
    if b == 1:
        return 1
    if a & 1 == 1:
        return f(a + 1, b) ^ f(0, a - 1)
    if b & 1 == 1:
        return f(a, b - 1) ^ f(0, b - 2)
    return f(a / 2, b / 2) * 2

if __name__ == '__main__':
    f()