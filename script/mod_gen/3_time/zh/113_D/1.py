def main():
    H,W,K = map(int,input().split())
    #print(H,W,K)
    dp = [[0 for i in range(W)] for j in range(H+1)]
    dp[0][0] = 1
    for i in range(1,H+1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == W-1:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][j] %= 1000000007
    print(dp[H][K-1])

if __name__ == '__main__':
    main()