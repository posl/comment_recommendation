def matchstick(N, M, A):
    #dp[i] = matchstick i can be made by the largest integer
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + match[a] <= N:
                dp[i + match[a]] = max(dp[i + match[a]], dp[i] * 10 + a)
    return dp[N]
