def main():
    # input
    H, W = map(int, input().split())
    Ss = [input() for _ in range(H)]
    # compute
    # dp[i][j] = (i, j) から右下に行くときの照らされるマスの最大値
    dp = [[0]*W for _ in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if Ss[i][j] == '#':
                continue
            if i == H-1 and j == W-1:
                dp[i][j] = 1
            elif i == H-1:
                dp[i][j] = dp[i][j+1] + 1
            elif j == W-1:
                dp[i][j] = dp[i+1][j] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + 1
    # output
    print(dp[0][0])
