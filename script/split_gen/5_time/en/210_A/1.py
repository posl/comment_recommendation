def buy_cabbage(N, A, X, Y):
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y
