def main():
    L = int(input())
    dp = [[0] * 201 for _ in range(201)]
    dp[0][0] = 1
    for i in range(1, L):
        for j in range(1, L):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    print(dp[L - 1][L - 1])
