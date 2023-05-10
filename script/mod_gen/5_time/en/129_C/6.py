def main():
    n,m = map(int,input().split())
    a = [int(input()) for i in range(m)]
    a.append(n+1)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n+1):
        for j in range(m+1):
            if i < a[j]:
                break
            dp[i] += dp[i-a[j]]
            dp[i] %= 10**9+7
    print(dp[n])

if __name__ == '__main__':
    main()