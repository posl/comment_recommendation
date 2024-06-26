def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    #print(N, M)
    #print(X)
    #print(C)
    #print(Y)
    dp = [0]*(N+1)
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(M):
            if i+C[j] > N:
                continue
            dp[i+C[j]] = max(dp[i+C[j]], dp[i]+Y[j])
    print(dp[N])

if __name__ == '__main__':
    main()