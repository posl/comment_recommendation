def main():
    #N M
    #X_1 X_2 ... X_N
    #C_1 Y_1
    #C_2 Y_2
    #.
    #.
    #.
    #C_M Y_M
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = []
    for i in range(M):
        CY.append(list(map(int, input().split())))
    #print(N, M)
    #print(X)
    #print(CY)
    #N, M = 6, 3
    #X = [2, 7, 1, 8, 2, 8]
    #CY = [[2, 10], [3, 1], [5, 5]]
    #dp[i][j] i番目までのコインでj回まで連続して表が出ている状態で得られる最大の金額
    #dp[i][j] = max(dp[i-1][j+1], dp[i-1][j]) + X[i]
    #dp[i][j] = max(dp[i-1][j+1], dp[i-1][j]) + Y[i]
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j]) + X[i]
    for i in range(N):
        for j in range(N):
            if i+1 == CY[j][0]:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j] + CY[j][1])
    #print(dp)
    print(max(dp[N]))

if __name__ == '__main__':
    main()