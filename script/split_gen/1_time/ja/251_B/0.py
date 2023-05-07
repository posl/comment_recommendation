def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (W + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(W - A[i], -1, -1):
            if dp[j] > 0:
                dp[j + A[i]] += dp[j]
    print(sum(dp))
