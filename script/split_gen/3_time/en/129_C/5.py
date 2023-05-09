def main():
    N, M = map(int, input().split())
    A = [int(input()) for i in range(M)]
    A.append(N+1)
    MOD = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N):
        if dp[i] == 0:
            continue
        for a in A:
            if i+a <= N:
                dp[i+a] += dp[i]
                dp[i+a] %= MOD
    print(dp[N])
    return
