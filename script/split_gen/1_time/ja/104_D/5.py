def main():
    S = input()
    Q = S.count("?")
    MOD = 10**9 + 7
    # dp[i][j][k]: i文字目まで見て、Aがj個、Bがk個あるときのABC数
    dp = [[[0 for _ in range(Q+1)] for _ in range(Q+1)] for _ in range(Q+1)]
    for i in range(len(S)):
        if S[i] == "A":
            dp[i+1][1][0] = (dp[i][0][0] + 1) % MOD
            dp[i+1][1][0] += dp[i][1][0]
            dp[i+1][1][0] %= MOD
            for j in range(1, Q+1):
                dp[i+1][j+1][0] = (dp[i][j][0] + 1) % MOD
                dp[i+1][j+1][0] += dp[i][j+1][0]
                dp[i+1][j+1][0] %= MOD
            for k in range(1, Q+1):
                dp[i+1][1][k] = (dp[i][0][k] + 1) % MOD
                dp[i+1][1][k] += dp[i][1][k]
                dp[i+1][1][k] %= MOD
        elif S[i] == "B":
            for j in range(1, Q+1):
                dp[i+1][j][1] = (dp[i][j][0] + 1) % MOD
                dp[i+1][j][1] += dp[i][j][1]
                dp[i+1][j][1] %= MOD
            for k in range(1, Q+1):
                dp[i+1][0][k] = (dp[i][0][k] + 1) % MOD
                dp[i+1][0][k] += dp[i][0][k-1]
                dp[i+1][0][k] %= MOD
            for j in range(1, Q+1):
                for k in range(1, Q+1):
                    dp[i+1][j][k] = (dp[i][j][
