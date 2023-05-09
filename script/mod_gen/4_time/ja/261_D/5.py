def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = []
    C = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    #print(N, M, X, Y, C)
    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            #print(i, j, dp[i][j])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            for k in range(M):
                if i + C[k] > N:
                    continue
                dp[i + C[k]][j + 1] = max(dp[i + C[k]][j + 1], dp[i][j] + Y[k])
    #print(dp)
    print(max(dp[N]))

if __name__ == '__main__':
    solve()