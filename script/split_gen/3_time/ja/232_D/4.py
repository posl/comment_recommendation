def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(list(input()))
    dp = [[0 for i in range(W)] for j in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1000000007
    print(dp[H - 1][W - 1])
