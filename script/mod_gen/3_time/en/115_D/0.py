def burger(n, x):
    if n == 0:
        return 1 if x > 0 else 0
    elif x == 1:
        return 0
    elif x <= 1 + 2 ** (n - 1):
        return burger(n - 1, x - 1)
    else:
        return burger(n - 1, x - 2 ** (n - 1) - 1) + 2 ** (n - 1)

if __name__ == '__main__':
    burger()