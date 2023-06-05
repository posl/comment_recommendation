def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [0] * 10
    dp[a[0]] = 1
    for i in range(n - 1):
        new_dp = [0] * 10
        for j in range(10):
            new_dp[(j + a[i + 1]) % 10] += dp[j]
            new_dp[(j + a[i + 1]) % 10] %= mod
            new_dp[(j * a[i + 1]) % 10] += dp[j]
            new_dp[(j * a[i + 1]) % 10] %= mod
        dp = new_dp
    for i in range(10):
        print(dp[i])

if __name__ == '__main__':
    main()