def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            dp[h][w] = max(dp[h + 1][w] + (1 if A[h][w] == '+' else -1), dp[h][w + 1] + (1 if A[h][w] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
