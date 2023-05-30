def solve():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        return T + D * (X - M)
    else:
        return T
print(solve())
