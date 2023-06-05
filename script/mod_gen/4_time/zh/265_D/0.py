def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, P, Q, R)
    #print(A)
    dp = [[0 for _ in range(3)] for _ in range(N)]
    dp[0][0] = P * A[0]
    dp[0][1] = dp[0][0] + Q * A[0]
    dp[0][2] = dp[0][1] + R * A[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0], P * A[i])
        dp[i][1] = max(dp[i - 1][1], dp[i][0] + Q * A[i])
        dp[i][2] = max(dp[i - 1][2], dp[i][1] + R * A[i])
    print(dp[-1][2])
solve()
