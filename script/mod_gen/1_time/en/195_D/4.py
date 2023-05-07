def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        available = X[:L-1] + X[R:]
        available.sort()
        available.reverse()
        available = [0] + available
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, M+1):
                if W[i-1] <= available[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + V[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp[N][M])

if __name__ == '__main__':
    main()