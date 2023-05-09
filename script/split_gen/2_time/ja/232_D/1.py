def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1] % (10 ** 9 + 7))
