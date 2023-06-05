def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 1024
        dp[0] = 1
        for j in range(n):
            for k in range(1023, -1, -1):
                if dp[k] == 0:
                    continue
                if j == n - 1:
                    if k | (1 << a[j]) == (1 << 10) - 1:
                        ans[i] += dp[k]
                        ans[i] %= mod
                else:
                    dp[k | (1 << a[j])] += dp[k]
                    dp[k | (1 << a[j])] %= mod
                    dp[k] *= 2
                    dp[k] %= mod
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()