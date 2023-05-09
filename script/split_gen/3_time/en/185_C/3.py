def main():
    L = int(input())
    dp = [[0 for _ in range(L+1)] for _ in range(L+1)]
    dp[0][0] = 1
    for i in range(1, L+1):
        for j in range(0, L+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-i]
    print(dp[L][L] - 1)
