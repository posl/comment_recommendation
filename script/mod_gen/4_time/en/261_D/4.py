def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = []
    Y = []
    for _ in range(M):
        c,y = map(int,input().split())
        C.append(c)
        Y.append(y)
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i])
            if j+1 in C:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j]+Y[C.index(j+1)])
    print(max(dp[N]))
main()

if __name__ == '__main__':
    main()