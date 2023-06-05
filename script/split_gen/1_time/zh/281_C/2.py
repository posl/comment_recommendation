def getSong(T, A, N):
    total = sum(A)
    T = T % total
    i = 0
    while T > 0:
        T = T - A[i]
        i += 1
    return i, T + A[i - 1]
