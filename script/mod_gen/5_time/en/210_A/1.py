def buy_cabbage(N, A, X, Y):
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y

if __name__ == '__main__':
    buy_cabbage()