def main():
    S = input()
    MOD = 10**9 + 7
    Q = S.count('?')
    dp = [[0]*3 for _ in range(Q+1)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        if s == '?':
            for j in range(3):
                for k in range(3):
                    dp[i+1][j] += dp[i][k]
                    dp[i+1][j] %= MOD
        else:
            for j in range(3):
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD
            if s == 'A':
                dp[i+1][1] += dp[i][0]
                dp[i+1][1] %= MOD
            elif s == 'B':
                dp[i+1][2] += dp[i][1]
                dp[i+1][2] %= MOD
            else:
                dp[i+1][0] += dp[i][2]
                dp[i+1][0] %= MOD
    print(dp[Q][0])

if __name__ == '__main__':
    main()