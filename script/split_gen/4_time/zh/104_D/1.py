def solve():
    S = input()
    Q = S.count("?")
    mod = 10**9 + 7
    dp = [[0 for _ in range(3)] for _ in range(3)]
    dp[0][0] = 1
    for i in range(len(S)):
        if S[i] == 'A':
            dp[1][0] += dp[0][0]
            dp[1][1] += dp[0][1]
            dp[1][2] += dp[0][2]
        elif S[i] == 'B':
            dp[2][0] += dp[1][0]
            dp[2][1] += dp[1][1]
            dp[2][2] += dp[1][2]
        elif S[i] == 'C':
            dp[0][0] += dp[2][0]
            dp[0][1] += dp[2][1]
            dp[0][2] += dp[2][2]
        else:
            dp[1][0] += dp[0][0]
            dp[1][1] += dp[0][1]
            dp[1][2] += dp[0][2]
            dp[2][0] += dp[1][0]
            dp[2][1] += dp[1][1]
            dp[2][2] += dp[1][2]
            dp[0][0] += dp[2][0]
            dp[0][1] += dp[2][1]
            dp[0][2] += dp[2][2]
        for j in range(3):
            dp[j][0] %= mod
            dp[j][1] %= mod
            dp[j][2] %= mod
    print(dp[0][2] % mod)
