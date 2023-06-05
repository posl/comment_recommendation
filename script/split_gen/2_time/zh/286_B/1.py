def swap(A, P, Q, R, S):
    B = []
    for i in range(0, len(A)):
        if i == P-1:
            for j in range(R-1, S):
                B.append(A[j])
        elif i == R-1:
            for j in range(P-1, Q):
                B.append(A[j])
        else:
            B.append(A[i])
    return B
