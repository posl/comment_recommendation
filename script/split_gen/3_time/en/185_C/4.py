def main():
    L = int(input())
    dp = [[0 for _ in range(L+1)] for _ in range(L+1)]
    dp[0][0] = 1
    for i in range(1,L+1):
        for j in range(i,L+1):
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] += dp[i][j-1]
    print(dp[L][L]-1)
