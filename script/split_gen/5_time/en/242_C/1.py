def main():
    N = int(input())
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(10):
            for k in range(10):
                if abs(j-k) > 1:
                    continue
                dp[i+1][j] += dp[i][k]
                dp[i+1][j] %= 998244353
    print(sum(dp[N])%998244353)
