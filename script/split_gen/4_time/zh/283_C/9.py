def main():
    S = input()
    N = len(S)
    # dp[i][j] := S[i] まで決めて, j を作るのに必要な操作の最小値
    dp = [[float('inf')] * 21 for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(21):
            if dp[i][j] == float('inf'):
                continue
            if S[i] == '0':
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            else:
                dp[i + 1][(j + int(S[i])) % 21] = min(dp[i + 1][(j + int(S[i])) % 21], dp[i][j] + 1)
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    print(dp[N][5])
