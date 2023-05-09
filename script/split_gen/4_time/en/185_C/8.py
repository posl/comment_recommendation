def main():
    L = int(input())
    mod = 10**9 + 7
    # dp[i][j] := i本の棒に分割する場合の数
    dp = [[0] * (L + 1) for _ in range(L + 1)]
    dp[0][0] = 1
    for i in range(L):
        for j in range(L + 1):
            if j > i:
                continue
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j + 1] += dp[i][j] * (i - j + 1)
            dp[i + 1][j + 1] %= mod
    print(dp[L][L])
