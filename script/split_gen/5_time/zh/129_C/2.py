def main():
    N, M = map(int, input().split())
    A = [int(input()) for i in range(M)]
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i not in A:
            if i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
                dp[i] %= 1000000007
    print(dp[N])
