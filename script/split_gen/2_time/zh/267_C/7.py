def solve(n, m, A):
    B = [0] * n
    for i in range(n - 1):
        if A[i + 1] > A[i]:
            B[i] = 1
        elif A[i + 1] < A[i]:
            B[i] = -1
    print(B)
    if m == 1:
        return max(A)
    if m == 2:
        return max(A[0] + 2 * A[1], 2 * A[0] + A[1])
    dp = [0] * n
    dp[0] = 0
    dp[1] = max(0, B[0] + 2 * B[1])
    for i in range(2, n):
        dp[i] = max(0, dp[i - 2] + B[i - 1] + 2 * B[i], dp[i - 1] + B[i] + 2 * B[i - 1])
    print(dp)
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, sum([j * B[i + j] for j in range(m)]))
    return ans
