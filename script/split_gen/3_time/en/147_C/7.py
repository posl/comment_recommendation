def check(i, A, x, y, honest):
    for j in range(A[i]):
        if honest[x[i][j] - 1] != y[i][j]:
            return False
    return True
