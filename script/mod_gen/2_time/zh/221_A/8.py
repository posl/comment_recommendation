def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        for j in range(10):
            dp[(i + j) % 10] += 1
        for k in range(n - 1):
            tmp = [0] * 10
            for j in range(10):
                tmp[(j * a[k + 1]) % 10] += dp[j]
                tmp[(j + a[k + 1]) % 10] += dp[j]
            dp = tmp
        for j in range(10):
            ans[j] = (ans[j] + dp[j]) % mod
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()