def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K[i]):
            dp[A[i][j]] = max(dp[A[i][j]], dp[i] + T[i])
    ans = max(dp) + T[N]
    print(ans)
