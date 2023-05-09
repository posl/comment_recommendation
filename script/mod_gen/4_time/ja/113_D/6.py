def solve():
    H, W, K = map(int, input().split())
    #dp[i][j] := i段目にいて、j番目の縦線にいる場合の数
    dp = [[0 for j in range(W)] for i in range(H+1)]
    dp[0][0] = 1
    for i in range(1, H+1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == W-1:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][j] %= 1000000007
    print(dp[H][K-1])

if __name__ == '__main__':
    solve()