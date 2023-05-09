def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [float('inf')] * N
    dp[0] = T[0]
    for i in range(N):
        dp[i] = min(dp[i], dp[i-1] + T[i])
        for j in range(K[i]):
            dp[A[i][j]-1] = min(dp[A[i][j]-1], dp[i])
    print(dp[N-1])
