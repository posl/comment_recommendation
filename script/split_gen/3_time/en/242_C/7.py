def main():
    N = int(input())
    mod = 998244353
    dp = [[[0]*10 for _ in range(10)] for _ in range(N+1)]
    for i in range(1,10):
        dp[1][i][i] = 1
    for i in range(2,N+1):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    if abs(j-k) <= 1:
                        dp[i][j][k] += dp[i-1][l][j]
                        dp[i][j][k] %= mod
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += dp[N][i][j]
            ans %= mod
    print(ans)
