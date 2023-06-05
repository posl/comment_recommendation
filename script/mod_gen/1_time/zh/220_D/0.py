def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(0, n - 1):
            ndp = [0] * 10
            for k in range(10):
                ndp[(k + a[j]) % 10] += dp[k]
                ndp[(k * a[j]) % 10] += dp[k]
            dp = ndp
        ans[i] = dp[0]
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()