def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    #print(N, M)
    #print(X)
    #print(C)
    #print(Y)
    dp = [[-1 for i in range(N+1)] for j in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            #print(i, j, dp[i][j])
            # 表
            if i+1 <= N:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i])
            # 裏
            if i+1 <= N:
                dp[i+1][0] = max(dp[i+1][0], dp[i][j])
            # ボーナス
            for k in range(M):
                if j+1 == C[k]:
                    dp[i+1][0] = max(dp[i+1][0], dp[i][j]+Y[k])
    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[N][i])
    print(ans)

if __name__ == '__main__':
    main()