def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    # dp[i][j] = i番目までの要素からj個選んだ時の総和
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j] %= mod
            dp[i + 1][j + 1] += dp[i][j] * A[i]
            dp[i + 1][j + 1] %= mod
    ans = 0
    for i in range(N):
        ans += dp[N][i + 1] * A[i]
        ans %= mod
    print(ans)
