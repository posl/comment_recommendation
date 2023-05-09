def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    # dp[i][j] := (1,1) から (i,j) までの最短距離
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            dp[i][j] += 1
    print(dp[-1][-1])
