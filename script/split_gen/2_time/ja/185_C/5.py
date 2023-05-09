def main():
    L = int(input())
    # dp[i][j] := i 本の棒を j 本に分割する場合の数
    dp = [[0] * (L + 1) for _ in range(L + 1)]
    dp[0][0] = 1
    for i in range(1, L + 1):
        for j in range(1, i + 1):
            for k in range(i):
                dp[i][j] += dp[k][j - 1] * dp[i - k - 1][j]
    print(dp[L][L])
