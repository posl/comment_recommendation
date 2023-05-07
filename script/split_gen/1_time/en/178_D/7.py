def main():
    S = int(input())
    MOD = 1000000007
    # dp[i][j] = number of sequences whose sum is i and last term is j
    dp = [[0] * (S + 1) for _ in range(S + 1)]
    dp[0][0] = 1
    for i in range(1, S + 1):
        for j in range(1, S + 1):
            if i - j >= 0:
                dp[i][j] = (dp[i - j][j] + dp[i][j - 1]) % MOD
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[S][S])
