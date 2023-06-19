def solve():
    S = input()
    # DP
    # dp[i][j] 表示 S[:i] 中有多少个数模 13 余 j
    # dp[i][j] = dp[i-1][j] * 10 + dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][j-9]
    # dp[0][0] = 1
    # dp[0][j] = 0
    # 由于 dp[i][j] 只取决于 dp[i-1][j]，所以可以优化成一维数组
    n = len(S)
    dp = [0] * 13
    dp[0] = 1
    for i in range(n):
        if S[i] == '?':
            # dp[i][j] = dp[i-1][j] * 10 + dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][j-9]
            dp = [(dp[j] * 10 + dp[j-1] + dp[j-2] + dp[j-3] + dp[j-4] + dp[j-5] + dp[j-6] + dp[j-7] + dp[j-8] + dp[j-9]) % (10**9+7) for j in range(13)]
        else:
            # dp[i][j] = dp[i-1][j] + dp[i-1][j-10] + dp[i-1][j-20] + ... + dp[i-1][j-90]
            dp = [(dp[j] + dp[j-10] + dp[j-20] + dp[j-30] + dp[j-40] + dp[j-50] + dp[j-60] + dp[j-70] + dp[j-80] + dp[j-90]) % (10**9+7) for j in range(13)]
            if S[i] == '0':
                dp = [dp[j] - dp[j-10] for j in range(13)]
    print(dp[5])
