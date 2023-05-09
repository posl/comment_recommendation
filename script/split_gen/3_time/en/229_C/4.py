def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(N, W)
    #print(A)
    #print(B)
    #dp = [[0] * (W+1)] * (N+1)
    dp = [[0] * (W+1) for i in range(N+1)]
    #print(dp)
    for i in range(N):
        for j in range(W+1):
            if j - B[i] >= 0:
                dp[i+1][j] = max(dp[i][j-B[i]] + A[i], dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print(dp[N][W])
