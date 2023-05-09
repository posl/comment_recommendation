def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A.append(0)
    A.append(N+1)
    A.sort()
    MOD = 10**9+7
    dp = [0]*(N+2)
    dp[0] = 1
    for i in range(1, N+2):
        if A[0] == i:
            A.pop(0)
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD
    print(dp[-1])
