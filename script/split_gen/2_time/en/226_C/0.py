def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(N):
        dp[i + 1] = min(dp[i + 1], dp[i] + T[i])
        for j in A[i]:
            dp[i + 1] = min(dp[i + 1], dp[j] + T[i])
    print(dp[N])
