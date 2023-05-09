def main():
    H, W = [int(x) for x in input().split()]
    A = [input() for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if (i + j) % 2 == 0:
                if A[i][j] == '+':
                    dp[i][j] = max(dp[i + 1][j] + 1, dp[i][j + 1] + 1)
                else:
                    dp[i][j] = min(dp[i + 1][j] - 1, dp[i][j + 1] - 1)
            else:
                if A[i][j] == '+':
                    dp[i][j] = min(dp[i + 1][j] - 1, dp[i][j + 1] - 1)
                else:
                    dp[i][j] = max(dp[i + 1][j] + 1, dp[i][j + 1] + 1)
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
