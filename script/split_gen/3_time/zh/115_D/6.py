def burger(N, X):
    if N == 0:
        return 0
    L = 2 ** (N + 1) - 3
    if X == 1:
        return 0
    elif X <= 1 + L:
        return burger(N - 1, X - 1)
    elif X == 2 + L:
        return 1 + burger(N - 1, X - 2 - L)
    elif X <= 2 * (1 + L):
        return 1 + burger(N - 1, X - 2 - L)
    else:
        return 2 ** N + burger(N - 1, X - 2 * (1 + L))
N, X = map(int, input().split())
print(burger(N, X))
