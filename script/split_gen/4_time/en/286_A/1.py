def swap(A, P, Q, R, S):
    B = []
    B.extend(A[0:P-1])
    B.extend(A[R-1:S])
    B.extend(A[Q:S-R+1])
    B.extend(A[P-1:Q])
    B.extend(A[S:len(A)])
    return B
