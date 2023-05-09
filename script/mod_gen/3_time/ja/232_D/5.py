def main():
    # H, W = map(int, input().split())
    # C = [input() for _ in range(H)]
    H, W = 5, 5
    C = [
        ".....",
        ".....",
        ".....",
        ".....",
        ".....",
    ]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1]
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[-1][-1])
main()

if __name__ == '__main__':
    main()