def burger(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    else:
        a = 2 ** (N + 3) - 3
        if X <= 1 + a // 2:
            return burger(N - 1, X - 1)
        elif X == 2 + a // 2:
            return 2 ** (N + 1) - 1
        else:
            return 2 ** (N + 1) - 1 + burger(N - 1, X - 2 - a // 2)
N, X = map(int, input().split())
print(burger(N, X))
