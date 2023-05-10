def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] := i番目までの数でj個の数を選んだときの総和
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] += dp[i][j] * A[i]
            dp[i + 1][j + 1] %= MOD
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
    ans = 0
    for i in range(1, N + 1):
        ans += dp[N][i]
        ans %= MOD
    print(ans)
