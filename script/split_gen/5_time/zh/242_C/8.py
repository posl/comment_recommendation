def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(N)]
    dp[0] = [1] * 10
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= mod
    print(sum(dp[N-1][1:]) % mod)
