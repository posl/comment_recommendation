def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A.append(N)
    A.append(N+1)
    A.sort()
    dp = [0] * (N + 2)
    dp[0] = 1
    for i in range(1, N + 2):
        if i in A:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[N + 1] % 1000000007)
