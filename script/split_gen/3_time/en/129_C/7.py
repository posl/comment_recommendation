def main():
    n,m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    a.sort()
    if m == 0:
        print(1)
        exit()
    if a[0] == 1:
        print(0)
        exit()
    if m == 1:
        print(2)
        exit()
    if m == 2:
        print(1)
        exit()
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    i = 3
    j = 0
    while i <= n:
        if a[j] == i:
            j += 1
            i += 1
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
        i += 1
    print(dp[n])
    return
