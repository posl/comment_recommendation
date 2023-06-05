def f(a, b):
    if a == b:
        return a
    if a % 2 == 1:
        return f(a + 1, b) ^ a
    else:
        return f(a + 1, b)

if __name__ == '__main__':
    f()