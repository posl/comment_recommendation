def burger(N, X):
    if N == 0:
        return 1 if X > 0 else 0
    elif X == 1:
        return 0
    elif X <= 1 + 2 ** (N-1):
        return burger(N-1, X-1)
    elif X == 2 + 2 ** (N-1):
        return 2 ** N
    else:
        return 2 ** N + burger(N-1, X - 2 - 2 ** (N-1))

if __name__ == '__main__':
    burger()