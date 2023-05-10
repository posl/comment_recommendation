def solve():
    N, X, Y = map(int, input().split())
    if N == 1:
        print(0)
        return
    dp = [0] * (N + 1)
    dp[2] = X
    for i in range(3, N + 1):
        dp[i] = min(dp[i - 1] + X, dp[i - 2] + Y)
    print(dp[N])
    return
