def main():
    L = int(input())
    dp = [[0 for i in range(L+1)] for j in range(L+1)]
    dp[0][0] = 1
    for i in range(L):
        for j in range(L):
            if i+j+1 <= L:
                dp[i+j+1][j] += dp[i][j]
            dp[i][j+1] += dp[i][j]
    print(dp[L][0])
