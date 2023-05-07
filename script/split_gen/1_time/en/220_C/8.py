def solve(N, A, X):
    if sum(A) >= X:
        return 0
    B = A * 100
    k = 0
    s = 0
    while s < X:
        s += B[k]
        k += 1
    return k
