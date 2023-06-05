def f(h):
    if h == 1:
        return 1
    else:
        return 2 * f(h // 2) + 1

if __name__ == '__main__':
    f()