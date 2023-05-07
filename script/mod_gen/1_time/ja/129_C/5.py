def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    a = [0] + a + [n+1]
    a.sort()
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % (10**9+7)
    print(dp[n])

if __name__ == '__main__':
    main()