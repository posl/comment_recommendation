def solve():
    N, A, B = map(int, input().split())
    S = input()
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        dp[i] = dp[i-1] + A
        for j in range(1, i+1):
            if S[i-1] != S[i-j]:
                dp[i] = min(dp[i], dp[i-j] + B)
            else:
                dp[i] = min(dp[i], dp[i-j])
    print(dp[N])
