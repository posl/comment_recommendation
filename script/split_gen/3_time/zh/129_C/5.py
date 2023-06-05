def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A.append(N)
    dp = [0] * (N + 1)
    dp[0] = 1
    MOD = 10 ** 9 + 7
    for i in range(1, N + 1):
        if i in A:
            continue
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        dp[i] %= MOD
    print(dp[N])
