def main():
    H, W = list(map(int, input().strip().split()))
    C = [input().strip() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % 1000000007
    print(dp[H - 1][W - 1])
