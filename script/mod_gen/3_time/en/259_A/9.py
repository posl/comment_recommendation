def takahashiHeight(N, M, X, T, D):
    if (M < X):
        return T + (M * D)
    else:
        return T + (X * D) + ((M - X) * D)

if __name__ == '__main__':
    takahashiHeight()