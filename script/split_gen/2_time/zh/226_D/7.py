def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[0] * N for i in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        for j in range(1, K[i] + 1):
            A[i][j] = int(input())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, K[i] + 1):
            dp[i] = max(dp[i], dp[A[i][j]] + T[A[i][j]])
    print(dp[N] + T[N])
