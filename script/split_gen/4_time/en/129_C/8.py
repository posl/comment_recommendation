def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N+1)
    a.append(0)
    a.sort()
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(M+1):
        if a[i+1] - a[i] > 1:
            for j in range(a[i+1]-a[i]-1):
                dp[a[i]+j+1] = (dp[a[i]+j] + dp[a[i]+j-1]) % 1000000007
    print(dp[N])
