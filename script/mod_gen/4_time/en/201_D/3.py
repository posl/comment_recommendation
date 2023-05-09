def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 if A[0][0] == '+' else -1
    for i in range(1, H):
        if A[i][0] == '+':
            dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = dp[i - 1][0] - 1
    for j in range(1, W):
        if A[0][j] == '+':
            dp[0][j] = dp[0][j - 1] + 1
        else:
            dp[0][j] = dp[0][j - 1] - 1
    for i in range(1, H):
        for j in range(1, W):
            if A[i][j] == '+':
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            else:
                dp[i][j] = min(dp[i - 1][j] - 1, dp[i][j - 1] - 1)
    if dp[-1][-1] > 0:
        print('Takahashi')
    elif dp[-1][-1] < 0:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()