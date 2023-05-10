def swap(A, P, Q, R, S):
    B = A[:]
    for i in range(P-1, Q):
        B[i] = A[R-1+i-P]
    for i in range(R-1, S):
        B[i] = A[P-1+i-R]
    return B
