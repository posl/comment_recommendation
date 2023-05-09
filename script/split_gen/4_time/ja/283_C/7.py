def main():
    S = input()
    S = S[::-1]
    S = list(S)
    S = [int(i) for i in S]
    n = len(S)
    dp = [[float('inf') for _ in range(2)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        # i桁目が0の場合
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + S[i])
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + S[i] + 1)
        # i桁目が1の場合
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + 10 - S[i])
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + 10 - S[i] - 1)
    print(dp[n][0])
