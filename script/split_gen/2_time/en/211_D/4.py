def solve():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        E[a].append(b)
        E[b].append(a)
    MOD = 10**9 + 7
    # dp[i]: i番目の都市にいるときのパスの数
    dp = [0] * N
    dp[0] = 1
    for i in range(N-1):
        for j in E[i]:
            dp[j] += dp[i]
            dp[j] %= MOD
    print(dp[N-1])
    return
