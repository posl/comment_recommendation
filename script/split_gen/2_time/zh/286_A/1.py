def swap(A, P, Q, R, S):
    B = A.copy()
    for i in range(P-1, Q):
        B[i] = A[R+i-Q]
    for i in range(R-1, S):
        B[i] = A[P+i-R]
    return B
