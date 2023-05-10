def main():
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10):
            for k in range(10):
                if abs(j-k) <= 1:
                    dp[i+1][j] = (dp[i+1][j]+dp[i][k])%998244353
    print(sum(dp[n])%998244353)
