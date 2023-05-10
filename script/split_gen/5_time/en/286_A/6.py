def swapAtoB(A, P, Q, R, S):
    A[P-1:Q], A[R-1:S] = A[R-1:S], A[P-1:Q]
    return A
