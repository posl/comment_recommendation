def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [float("inf")] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + T[i])
        for j in range(K[i]):
            dp[i] = min(dp[i], dp[A[i][j] - 1] + T[i])
    print(dp[N - 1])
