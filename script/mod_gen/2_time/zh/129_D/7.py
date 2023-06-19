def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # S[i][j] = 1 if S[i][j] == '.' else 0
    # dp[i][j] = (dp[i][j-1] if S[i][j-1] == '.' else 0) + (dp[i-1][j] if S[i-1][j] == '.' else 0) + (dp[i-1][j-1] if S[i-1][j-1] == '.' else 0) + S[i][j]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1 if S[0][0] == '.' else 0
    for i in range(1, H):
        dp[i][0] = dp[i-1][0] if S[i-1][0] == '.' else 0
    for j in range(1, W):
        dp[0][j] = dp[0][j-1] if S[0][j-1] == '.' else 0
    for i in range(1, H):
        for j in range(1, W):
            dp[i][j] = (dp[i][j-1] if S[i][j-1] == '.' else 0) + (dp[i-1][j] if S[i-1][j] == '.' else 0) + (dp[i-1][j-1] if S[i-1][j-1] == '.' else 0) + (1 if S[i][j] == '.' else 0)
    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()