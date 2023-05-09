def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i + 1 < H:
                dp[i + 1][j] += dp[i][j]
            if j + 1 < W:
                dp[i][j + 1] += dp[i][j]
    print(dp[-1][-1])

if __name__ == '__main__':
    main()