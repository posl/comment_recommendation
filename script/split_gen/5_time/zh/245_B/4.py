def find_min_positive_integer(N,A):
    A.sort()
    if A[0] > 0:
        return 0
    for i in range(0,N-1):
        if A[i] >= 0 and A[i+1] - A[i] > 1:
            return A[i] + 1
    return A[N-1] + 1
