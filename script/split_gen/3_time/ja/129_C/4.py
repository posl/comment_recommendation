def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    a.append(0)
    a.append(n+1)
    a.sort()
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[n])
