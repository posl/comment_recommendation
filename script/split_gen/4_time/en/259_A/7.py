def get_height(N, M, X, T, D):
    height = T
    for i in range(X, N):
        height += D
    return height
