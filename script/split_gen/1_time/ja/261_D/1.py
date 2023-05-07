def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for _ in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    #print(N, M)
    #print(X)
    #print(C, Y)
    #dp[i][j] := i回目までのコイントスで、カウンタの数値がjのときにもらえる最大金額
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j == 0:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i])
            else:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i] + Y[C.index(j)])
    #print(dp)
    print(max(dp[N]))
