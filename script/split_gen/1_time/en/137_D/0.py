def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A, B = zip(*sorted(zip(A, B), reverse=True))
    dp = [0] * (M + 1)
    for i in range(N):
        for j in range(M, 0, -1):
            if j - A[i] >= 0:
                dp[j] = max(dp[j], dp[j - A[i]] + B[i])
    print(dp[M])
