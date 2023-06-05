def solve():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    for i in range(1, N + 1):
        A[i].sort(reverse = True)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = T[i]
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j]] + T[i])
    print(dp[N])
solve()
