def solve():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
        K[i] -= 1
    # A[i] の要素を逆順にする
    for i in range(N):
        A[i].reverse()
    # dp[i] := 技 i を習得するのに必要な時間の最小値
    dp = [0] * N
    for i in range(N):
        if K[i] == -1: # 技 i が覚えるのに必要な技がない
            dp[i] = T[i]
            continue
        # 技 i が覚えるのに必要な技がある
        # 技 i が覚えるのに必要な技を先に習得する
        dp[i] = dp[A[i][0]] + T[i]
        for j in range(1, K[i]+1):
            dp[i] = min(dp[i], dp[A[i][j]] + T[i])
    print(dp[N-1])
solve()
