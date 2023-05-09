def solve(N,M,X):
    X.sort()
    if N >= M:
        return 0
    else:
        X_diff = [X[i+1] - X[i] for i in range(M-1)]
        X_diff.sort()
        return sum(X_diff[:M-N])
