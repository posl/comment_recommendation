def check(X, A, B, K):
    if X[0] not in [A[0], B[0]]:
        return False
    for i in range(1, len(X)):
        if X[i] not in [A[i], B[i]]:
            return False
        if abs(X[i]-X[i-1]) > K:
            return False
    return True
