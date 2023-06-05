def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(n+1):
        for j in range(m+1):
            if a[j] == i:
                dp[i] = 0
                break
            if a[j] > i:
                break
            dp[i] += dp[i-a[j]]
            dp[i] %= 1000000007
    print(dp[n])

if __name__ == '__main__':
    main()