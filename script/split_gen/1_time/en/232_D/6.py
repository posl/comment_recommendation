def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1])
    return
