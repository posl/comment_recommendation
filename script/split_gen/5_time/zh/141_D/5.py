def get_min_price(N, M, A):
    A.sort()
    A.reverse()
    for i in range(M):
        A[0] = A[0] >> 1
        A.sort()
        A.reverse()
    return sum(A)
