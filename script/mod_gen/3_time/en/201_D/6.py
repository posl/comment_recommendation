def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                if A[i][j] == '+':
                    dp[i][j] = 1
                else:
                    dp[i][j] = -1
                continue
            if i == 0:
                if A[i][j] == '+':
                    dp[i][j] = dp[i][j - 1] - 1
                else:
                    dp[i][j] = dp[i][j - 1] + 1
                continue
            if j == 0:
                if A[i][j] == '+':
                    dp[i][j] = dp[i - 1][j] - 1
                else:
                    dp[i][j] = dp[i - 1][j] + 1
                continue
            if A[i][j] == '+':
                dp[i][j] = max(dp[i - 1][j] - 1, dp[i][j - 1] - 1)
            else:
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    if dp[H - 1][W - 1] > 0:
        print('Takahashi')
    elif dp[H - 1][W - 1] < 0:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()