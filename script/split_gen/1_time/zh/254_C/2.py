def solve(N, K, A):
    A = sorted(A)
    for i in range(N-K):
        if A[i] >= A[i+K]:
            return "No"
    return "Yes"
