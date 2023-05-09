def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                if i == 0 and j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = -1
                elif i == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = dp[i][j - 1] - 1
                elif j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i - 1][j] + 1
                    else:
                        dp[i][j] = dp[i - 1][j] - 1
                else:
                    if A[i][j] == '+':
                        dp[i][j] = max(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                    else:
                        dp[i][j] = min(dp[i - 1][j] - 1, dp[i][j - 1] - 1)
            else:
                if i == 0 and j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = -1
                    else:
                        dp[i][j] = 1
                elif i == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i][j - 1] - 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
                elif j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i - 1][j] - 1
                    else:
                        dp[i][j] = dp[i - 1][j] + 1
                else:
                    if A[i][j] == '+':
                        dp[i][j] = min(dp[i - 1][

if __name__ == '__main__':
    main()