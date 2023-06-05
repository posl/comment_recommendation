def check(i, n, A, x, y, honest):
    for j in range(A[i]):
        if honest[x[i][j]] != -1 and honest[x[i][j]] != y[i][j]:
            return False
    return True
