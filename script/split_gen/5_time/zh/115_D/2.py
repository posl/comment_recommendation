def burger(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + burger(N - 1, N - 1):
        return burger(N - 1, X - 1)
    else:
        return 1 + burger(N - 1, X - 2 - burger(N - 1, N - 1))
