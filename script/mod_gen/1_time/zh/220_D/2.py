def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * n
        for j in range(n):
            if i == a[j]:
                dp[j] = 1
        for _ in range(n - 1):
            dp2 = [0] * (len(dp) - 1)
            for j in range(len(dp) - 1):
                dp2[j] = (dp[j + 1] + dp[j]) % mod
            dp = dp2
        ans[i] = dp[0]
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()