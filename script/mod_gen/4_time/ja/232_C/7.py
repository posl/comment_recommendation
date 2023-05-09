def f(n, x, y):
    if n == 0:
        return True
    for i in range(n):
        if x[i] != y[i]:
            return False
    return True

if __name__ == '__main__':
    f()