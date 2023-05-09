def solve():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            return 0 if N == 1 else -1
        else:
            return -1
    if D > 0:
        if X < A:
            return -1
        if X > A + D * (N - 1):
            return -1
        if X == A + D * (N - 1):
            return 0
        return (X - A) % D
    else:
        if X > A:
            return -1
        if X < A + D * (N - 1):
            return -1
        if X == A + D * (N - 1):
            return 0
        return (A - X) % (-D)
print(solve())
