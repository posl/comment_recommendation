def main():
    N, M = map(int, input().split())
    A = [int(input()) for i in range(M)]
    A.append(N)
    A = [0] + A
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(1, N+1):
        if i in A:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[N])
