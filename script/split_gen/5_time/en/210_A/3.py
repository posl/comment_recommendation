def buy_cabbage(N, A, X, Y):
    if N <= A:
        return X * N
    else:
        return A * X + (N - A) * Y
