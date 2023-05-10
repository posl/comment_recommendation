def main():
    n = int(input())
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10):
            for k in range(10):
                if abs(j-k) <= 1:
                    dp[i+1][j] += dp[i][k]
                    dp[i+1][j] %= mod
    ans = 0
    for i in range(10):
        ans += dp[n][i]
        ans %= mod
    print(ans)
