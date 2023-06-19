def solve():
    N = int(input())
    A = []
    for i in range(N):
        x, y, p = map(int, input().split())
        A.append((x, y, p))
    A.sort(key=lambda x: x[0] + x[1])
    dp = [float("inf")] * (N + 1)
    dp[0] = -float("inf")
    for i in range(N):
        dp[i + 1] = min(dp[i + 1], A[i][1] - A[i][0])
        for j in range(i):
            dp[i + 1] = min(dp[i + 1], dp[j] + A[i][1] + A[i][0] - A[j][1] - A[j][0])
    return dp[N]
