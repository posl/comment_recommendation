def main():
    #input
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C_Y = [list(map(int, input().split())) for _ in range(M)]
    #compute
    C_Y.sort(key=lambda x: x[0], reverse=True)
    C, Y = zip(*C_Y)
    dp = [0]*(N+1)
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(M):
            if i-C[j]>=0:
                dp[i+1] = max(dp[i+1], dp[i-C[j]]+X[i]+Y[j])
    #output
    print(dp[N])
