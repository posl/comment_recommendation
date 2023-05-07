def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = dp[i] + T[i]
        for j in range(K[i]):
            dp[i + 1] = min(dp[i + 1], dp[A[i][j]] + T[i])
    print(dp[N])
