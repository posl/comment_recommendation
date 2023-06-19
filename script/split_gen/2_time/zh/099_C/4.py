def problem099_c():
    N = int(input())
    dp = [0 for i in range(N+1)]
    for i in range(1, N+1):
        dp[i] = float('inf')
        k = 1
        while i >= k:
            dp[i] = min(dp[i], dp[i-k]+1)
            k *= 6
        k = 1
        while i >= k:
            dp[i] = min(dp[i], dp[i-k]+1)
            k *= 9
    print(dp[N])
