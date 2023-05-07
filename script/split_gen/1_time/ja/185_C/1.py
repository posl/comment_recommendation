def main():
    l = int(input())
    dp = [[0 for i in range(l+1)] for j in range(l+1)]
    dp[0][0] = 1
    for i in range(1, l+1):
        for j in range(l+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp[l][11])
