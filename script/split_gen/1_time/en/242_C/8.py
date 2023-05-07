def main():
    N = int(input())
    MOD = 998244353
    #dp[i][j] := i桁目まで見たときに、j=0: 未満フラグが立っている, j=1: 未満フラグが立っていない
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(1 if j else 10):
                dp[i + 1][j or k < 9] += dp[i][j]
                dp[i + 1][j or k < 9] %= MOD
    print((dp[N][0] + dp[N][1]) % MOD)
