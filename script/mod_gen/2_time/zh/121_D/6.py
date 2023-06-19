def f(a, b):
    if a == b:
        return a
    else:
        return f(a, b - 1) ^ b

if __name__ == '__main__':
    f()