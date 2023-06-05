def solve(N, L, R, A):
    # L, R, A = map(int, input().split())
    # A = list(map(int, input().split()))
    # N = len(A)
    # dp[i] = (A_i, A_{i+1}, ... A_N)での最小コスト
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(N):
        dp[i + 1] = min(dp[i + 1], dp[i] + A[i] * L)
        dp[i + 1] = min(dp[i + 1], dp[i] + R)
        if i + 1 < N:
            dp[i + 2] = min(dp[i + 2], dp[i] + A[i] * L + R)
        if i + 2 < N:
            dp[i + 3] = min(dp[i + 3], dp[i] + A[i] * L + R * 2)
        if i + 3 < N:
            dp[i + 4] = min(dp[i + 4], dp[i] + A[i] * L + R * 3)
        if i + 4 < N:
            dp[i + 5] = min(dp[i + 5], dp[i] + A[i] * L + R * 4)
        if i + 5 < N:
            dp[i + 6] = min(dp[i + 6], dp[i] + A[i] * L + R * 5)
        if i + 6 < N:
            dp[i + 7] = min(dp[i + 7], dp[i] + A[i] * L + R * 6)
        if i + 7 < N:
            dp[i + 8] = min(dp[i + 8], dp[i] + A[i] * L + R * 7)
        if i + 8 < N:
            dp[i + 9] = min(dp[i + 9], dp[i] + A[i] * L + R * 8)
        if i + 9 < N:
            dp[i + 10] = min(dp[i + 10], dp[i] + A[i] * L + R * 9)
        if i +
