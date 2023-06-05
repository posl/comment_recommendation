def solve(A, B, K):
    if K <= A:
        return (A-K, B)
    else:
        return (0, max(0, B-(K-A)))
