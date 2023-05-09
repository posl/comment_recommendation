def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for i in range(N)]
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        dp[i] = 10 ** 18
        for j in range(K[i]):
            dp[i] = min(dp[i], dp[A[i][j] - 1] + T[i])
    print(dp[0])
