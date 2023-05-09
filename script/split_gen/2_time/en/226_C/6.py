def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        A.append(a)
    dp = [float('inf')] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + T[i])
        for a in A[i]:
            dp[i] = min(dp[i], dp[a - 1] + T[i])
    print(dp[N - 1])
