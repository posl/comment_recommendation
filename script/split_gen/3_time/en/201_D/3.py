def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1] + 1 if A[i][j] == '+' else dp[i][j-1] - 1
            elif j == 0:
                dp[i][j] = dp[i-1][j] + 1 if A[i][j] == '+' else dp[i-1][j] - 1
            else:
                if A[i][j] == '+':
                    dp[i][j] = max(dp[i-1][j] + 1, dp[i][j-1] + 1)
                else:
                    dp[i][j] = min(dp[i-1][j] - 1, dp[i][j-1] - 1)
    if dp[-1][-1] > 0:
        print('Takahashi')
    elif dp[-1][-1] == 0:
        print('Draw')
    else:
        print('Aoki')
