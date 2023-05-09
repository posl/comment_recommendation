def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                dp[i][j] = 1 if A[i][j] == '+' else -1
            elif i == 0:
                dp[i][j] = dp[i][j-1] * (-1) if A[i][j] == '+' else dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j] * (-1) if A[i][j] == '+' else dp[i-1][j]
            else:
                if A[i][j] == '+':
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) * (-1)
    if dp[H-1][W-1] > 0:
        print('Takahashi')
    elif dp[H-1][W-1] < 0:
        print('Aoki')
    else:
        print('Draw')
