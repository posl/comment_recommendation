def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + A[i])
    print(dp[W])
