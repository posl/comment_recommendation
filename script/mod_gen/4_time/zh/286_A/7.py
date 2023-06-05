def swap(A, P, Q, R, S):
    B = A.copy()
    for i in range(P-1, Q):
        B[i] = A[i+R-Q]
    for i in range(R-1, S):
        B[i] = A[i+P-R]
    return B

if __name__ == '__main__':
    swap()