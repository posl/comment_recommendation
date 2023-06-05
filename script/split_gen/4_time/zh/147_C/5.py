def check(i, n, A, X, Y):
    honest = [0]*n
    honest[i] = 1
    for j in range(n):
        if not honest[j]:
            continue
        for k in range(A[j]):
            if honest[X[j][k]-1] != Y[j][k]:
                return False
    return True
