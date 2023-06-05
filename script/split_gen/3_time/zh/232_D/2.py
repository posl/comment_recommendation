def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    dp = [[0 for j in range(W)] for i in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1])
