def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A, B = zip(*sorted(zip(A, B)))
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + B[i] * A[i])
    print(dp[W])
