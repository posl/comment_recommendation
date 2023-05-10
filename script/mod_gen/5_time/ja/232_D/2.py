def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1 if C[0][0] == '.' else 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
    print(dp[H - 1][W - 1])

if __name__ == '__main__':
    main()