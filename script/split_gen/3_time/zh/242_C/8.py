def main():
    N = int(input())
    MOD = 998244353
    dp = [[0 for i in range(10)] for j in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(10):
            for k in range(10):
                if abs(j-k)<=1:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= MOD
    ans = 0
    for i in range(10):
        ans += dp[N][i]
        ans %= MOD
    print(ans)
