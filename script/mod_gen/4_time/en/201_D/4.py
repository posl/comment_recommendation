def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                dp[i][j] = 1 if a[i][j] == '+' else -1
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + 1 if a[i][j] == '+' else dp[i][j - 1] - 1
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + 1 if a[i][j] == '+' else dp[i - 1][j] - 1
            else:
                dp[i][j] = max(dp[i - 1][j] + 1 if a[i][j] == '+' else dp[i - 1][j] - 1, dp[i][j - 1] + 1 if a[i][j] == '+' else dp[i][j - 1] - 1)
    if dp[h - 1][w - 1] > 0:
        print('Takahashi')
    elif dp[h - 1][w - 1] < 0:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()