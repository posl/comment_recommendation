def f(a, b):
    if a == b:
        return a
    else:
        return b | f(a, b-1)

if __name__ == '__main__':
    f()