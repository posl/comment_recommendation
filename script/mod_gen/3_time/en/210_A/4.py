def buy_cabbage(N, A, X, Y):
    if N > A:
        return A * X + (N - A) * Y
    else:
        return N * X

if __name__ == '__main__':
    buy_cabbage()