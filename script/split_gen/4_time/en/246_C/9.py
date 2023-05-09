def solve(N, K, X, A):
    A = sorted(A)
    A = [0] + A
    ans = 0
    for i in range(N, 0, -1):
        if A[i] - A[i - 1] <= K * X:
            K -= (A[i] - A[i - 1]) // X
            ans += A[i] - A[i - 1]
        else:
            ans += K * X
            K = 0
            break
    ans += K * X
    return ans
