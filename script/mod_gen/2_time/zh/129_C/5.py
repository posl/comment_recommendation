def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    a.append(n)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i not in a:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print(dp[n])

if __name__ == '__main__':
    main()