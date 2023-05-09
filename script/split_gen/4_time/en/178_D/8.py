def main():
    S = int(input())
    mod = 10**9+7
    # dp[i][j] i番目までの数値の和がjになる場合の数
    dp = [[0 for _ in range(S+1)] for _ in range(S+1)]
    # i=0のときはdp[0][0]だけ1
    dp[0][0] = 1
    # i=1のときはdp[1][3]だけ1
    dp[1][3] = 1
    for i in range(2, S+1):
        for j in range(3, S+1):
            dp[i][j] = dp[i-1][j-3]
            if j >= i and dp[i][j] > 0:
                dp[i][j] += dp[i][j-i]
    print(dp[S][S]%mod)
