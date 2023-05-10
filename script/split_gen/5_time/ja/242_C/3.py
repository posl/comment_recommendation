def main():
    N = int(input())
    dp = [[0 for i in range(10)] for j in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(10):
            if j-1 >= 0:
                dp[i+1][j-1] += dp[i][j]
            if j+1 <= 9:
                dp[i+1][j+1] += dp[i][j]
    print(sum(dp[N-1])%998244353)
