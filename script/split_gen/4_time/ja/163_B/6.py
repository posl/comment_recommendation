def solve(N, M, A):
    if N < sum(A):
        return -1
    else:
        return N - sum(A)
