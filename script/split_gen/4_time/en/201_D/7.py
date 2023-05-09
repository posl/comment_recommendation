def solve():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 if A[0][0] == '+' else -1
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                continue
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i - 1][j] + (1 if A[i][j] == '+' else -1), dp[i][j - 1] + (1 if A[i][j] == '+' else -1))
            else:
                dp[i][j] = min(dp[i - 1][j] - (1 if A[i][j] == '+' else -1), dp[i][j - 1] - (1 if A[i][j] == '+' else -1))
    if dp[H - 1][W - 1] > 0:
        print('Takahashi')
    elif dp[H - 1][W - 1] < 0:
        print('Aoki')
    else:
        print('Draw')
