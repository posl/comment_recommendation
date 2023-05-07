def main():
    n = int(input())
    T = [0] * n
    K = [0] * n
    A = [[] for _ in range(n)]
    for i in range(n):
        t, k = map(int, input().split())
        T[i] = t
        K[i] = k
        a = list(map(int, input().split()))
        A[i] = a
    dp = [0] * n
    for i in range(n):
        dp[i] = T[i]
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j] - 1] + T[i])
    print(dp[n - 1])
