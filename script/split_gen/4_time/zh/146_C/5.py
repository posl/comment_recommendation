def d(n):
    if n < 10:
        return 1
    else:
        return d(n // 10) + 1
A, B, X = map(int, input().split())
