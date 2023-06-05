def isHurt(N, S, D, X, Y):
    for i in range(N):
        if X[i] < S and Y[i] > D:
            return True
    return False
