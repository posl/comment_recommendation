def main():
    N = int(input())
    dp = [N] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        for j in [1, 6, 36, 216, 1296, 7776, 46656, 9, 81, 729, 6561, 59049]:
            if i >= j:
                dp[i] = min(dp[i], dp[i-j]+1)
    print(dp[N])
