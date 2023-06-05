def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(1, b)
    if a % 2 == 1 and b % 2 == 1:
        return f(a / 2, b / 2) * 4 + 3
    if a % 2 == 1 and b % 2 == 0:
        return f(a / 2, b / 2) * 4 + 2
    if a % 2 == 0 and b % 2 == 1:
        return f(a / 2, b / 2) * 4 + 1
    if a % 2 == 0 and b % 2 == 0:
        return f(a / 2, b / 2) * 4

if __name__ == '__main__':
    f()