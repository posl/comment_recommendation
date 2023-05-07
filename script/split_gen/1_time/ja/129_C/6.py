def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A = [0]+A
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N):
        if i+1 in A:
            continue
        if i+2 in A:
            dp[i+1] = dp[i]
        else:
            dp[i+1] = dp[i]+dp[i-1]
    print(dp[N]%(10**9+7))
