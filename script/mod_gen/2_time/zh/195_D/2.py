def solve():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        ans = 0
        for j in range(M):
            if j < L or j > R:
                ans += X[j]
        dp = [[0 for _ in range(ans+1)] for _ in range(N+1)]
        for i in range(N):
            for j in range(ans+1):
                if j - X[i] >= 0:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-X[i]]+V[i])
                else:
                    dp[i+1][j] = dp[i][j]
        print(dp[N][ans])

if __name__ == '__main__':
    solve()