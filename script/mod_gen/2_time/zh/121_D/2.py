def f(a, b):
    if a == 0:
        return g(b)
    else:
        return g(b) ^ g(a-1)

if __name__ == '__main__':
    f()