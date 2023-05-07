def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0 for _ in range(N)]
    Y = [0 for _ in range(N)]
    for _ in range(M):
        c, y = map(int, input().split())
        C[c-1] = c
        Y[c-1] = y
    dp = [0 for _ in range(N+1)]
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        dp[C[i]] = max(dp[C[i]], dp[i]+Y[i])
    print(dp[N])

if __name__ == '__main__':
    main()