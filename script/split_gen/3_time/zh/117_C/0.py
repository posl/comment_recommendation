def solve(N, M, X_1, X_2, X_M):
    X_M.sort()
    #print(X_M)
    if N == 1:
        return 0
    elif N == 2:
        return X_M[-1] - X_M[0]
    else:
        min = 100000000000000
