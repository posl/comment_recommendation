def get_honest_persons(N, A, X, Y):
    honest_persons = 0
    for i in range(N):
        honest = True
        for j in range(A[i]):
            if Y[i][j] == 1 and Y[X[i][j]-1][X[X[i][j]-1].index(i+1)] == 0:
                honest = False
        if honest:
            honest_persons += 1
    return honest_persons
