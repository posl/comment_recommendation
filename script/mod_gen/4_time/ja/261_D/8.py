def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for _ in range(M)]
    # dp[i] := i回目のコイントスまでの最大の金額
    dp = [0] * (N + 1)
    # dp[i] = max(dp[i], dp[i - 1] + X[i - 1])
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + X[i - 1]
    # dp[i] = max(dp[i], dp[i - C] + Y)
    for C, Y in CY:
        for i in range(C, N + 1):
            dp[i] = max(dp[i], dp[i - C] + Y)
    return dp[N]
print(solve())

if __name__ == '__main__':
    solve()