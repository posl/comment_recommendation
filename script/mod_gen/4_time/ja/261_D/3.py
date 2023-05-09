def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = []
    Y = []
    for _ in range(M):
        c,y = map(int,input().split())
        C.append(c)
        Y.append(y)
    
    #dp[i][j] i番目までのコインでj回表が出た時の最大金額
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(N+1):
            if j == 0:
                dp[i+1][j] = max(dp[i][j],dp[i+1][j])
            else:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j-1]+X[i])
            for k in range(M):
                if C[k] == j:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][0]+Y[k])
    print(max(dp[N]))

if __name__ == '__main__':
    main()