def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,N+1):
        for j in range(0,10):
            if j == 0:
                dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % mod
            elif j == 9:
                dp[i][9] = (dp[i-1][8] + dp[i-1][9]) % mod
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % mod
    ans = 0
    for i in range(10):
        ans += dp[N][i]
        ans %= mod
    print(ans)
