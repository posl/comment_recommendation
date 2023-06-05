def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if (i + j) % 2 == 0:
                if (i + 1) < h:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + (1 if a[i + 1][j] == '-' else -1))
                if (j + 1) < w:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + (1 if a[i][j + 1] == '-' else -1))
            else:
                if (i + 1) < h:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] - (1 if a[i + 1][j] == '-' else -1))
                if (j + 1) < w:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] - (1 if a[i][j + 1] == '-' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
