def main():
    n = int(input())
    dp = [[0 for i in range(10)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(10):
            for k in range(10):
                if abs(j-k) <= 1:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= 998244353
    ans = 0
    for i in range(10):
        ans += dp[n][i]
        ans %= 998244353
    print(ans)
