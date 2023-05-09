def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    dp = [0] * (W + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(W, A[i] - 1, -1):
            dp[j] = dp[j] + dp[j - A[i]]
    print(dp[W])
