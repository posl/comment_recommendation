def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j] + (1 if A[i][j] == '+' else -1), dp[i][j + 1] + (1 if A[i][j] == '+' else -1))
            else:
                dp[i][j] = min(dp[i + 1][j] - (1 if A[i][j] == '+' else -1), dp[i][j + 1] - (1 if A[i][j] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] == 0:
        print('Draw')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()