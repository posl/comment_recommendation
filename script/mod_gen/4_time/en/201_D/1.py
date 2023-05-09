def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
            if A[i][j] == '+':
                dp[i + 1][j + 1] += 1
            else:
                dp[i + 1][j + 1] -= 1
    if dp[H][W] == 0:
        print('Draw')
    elif dp[H][W] > 0:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()