def buy_cabbage(N, A, X, Y):
    if N > A:
        return A * X + (N - A) * Y
    else:
        return N * X
N, A, X, Y = map(int, input().split())
print(buy_cabbage(N, A, X, Y))
