def check(honest, N, A, x, y):
    for i in range(N):
        if (honest >> i) & 1:
            for j in range(A[i]):
                if (((honest >> (x[i][j] - 1)) & 1) ^ y[i][j]) != 0:
                    return False
    return True
