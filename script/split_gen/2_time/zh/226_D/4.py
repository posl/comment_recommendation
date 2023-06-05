def solve():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        line = list(map(int, input().split()))
        T[i] = line[0]
        K[i] = line[1]
        A[i] = line[2:]
    dp = [0] * N
    for i in range(N):
        if not A[i]:
            dp[i] = T[i]
        else:
            dp[i] = min([dp[a] for a in A[i]]) + T[i]
    print(max(dp))
