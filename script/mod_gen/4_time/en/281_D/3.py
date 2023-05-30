def solve():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K):
            if dp[i][j]:
                dp[i + 1][j] = 1
                if dp[i + 1][j + 1] < A[i]:
                    dp[i + 1][j + 1] = A[i]
    ans = 0
    for i in range(K, -1, -1):
        if dp[N][i] != 0 and dp[N][i] % D == 0:
            ans = dp[N][i]
            break
    if ans == 0:
        print(-1)
    else:
        print(ans)
solve()
