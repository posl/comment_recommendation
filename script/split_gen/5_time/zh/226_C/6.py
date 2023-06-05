def solve():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
        A[i] = [a - 1 for a in A[i]]
    dp = [0] * N
    for i in range(N):
        if not A[i]:
            dp[i] = T[i]
        else:
            for j in A[i]:
                dp[i] = max(dp[i], dp[j] + T[i])
    print(max(dp))
