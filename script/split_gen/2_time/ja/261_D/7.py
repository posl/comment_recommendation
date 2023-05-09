def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for _ in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [0] * (N+1)
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i] + X[i])
        for j in range(M):
            if i - C[j] >= 0:
                dp[i+1] = max(dp[i+1], dp[i-C[j]] + Y[j])
    print(dp[-1])
