def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(int(input()))
    A.append(N+1)
    A.append(0)
    A.sort()
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])
