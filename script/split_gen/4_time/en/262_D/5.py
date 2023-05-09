def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] = i番目までの要素からj個選んだ時の総和
    dp = [[0 for j in range(N+1)] for i in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(i+1):
            dp[i][j] += dp[i-1][j] * 2
            dp[i][j] %= MOD
            if j-1 >= 0:
                dp[i][j] += dp[i-1][j-1] * A[i-1]
                dp[i][j] %= MOD
    ans = 0
    for j in range(1, N+1):
        ans += dp[N][j]
        ans %= MOD
    print(ans)
