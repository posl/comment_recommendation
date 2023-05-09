def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    mod = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1 if 1 not in a else 0
    for i in range(2, N + 1):
        if i in a:
            continue
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[N])
