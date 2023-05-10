def buy_cabbage(N, A, X, Y):
    if N <= A:
        return X * N
    else:
        return A * X + (N - A) * Y

if __name__ == '__main__':
    buy_cabbage()