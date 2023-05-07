def takahashi_height(N, M, X, T, D):
    height = T
    for i in range(1, X):
        height += D
    for i in range(X, N):
        height += D
    return height
