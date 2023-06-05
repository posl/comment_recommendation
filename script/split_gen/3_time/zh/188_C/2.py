def tournament(A):
    N = len(A)
    B = [0] * N
    for i in range(N):
        B[i] = [A[i], i]
    return B
