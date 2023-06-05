def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(n - 1):
            nxt = [0] * 10
            for k in range(10):
                nxt[(k + a[j]) % 10] = (nxt[(k + a[j]) % 10] + dp[k]) % mod
                nxt[(k * a[j]) % 10] = (nxt[(k * a[j]) % 10] + dp[k]) % mod
            dp = nxt
        for j in range(10):
            ans[j] = (ans[j] + dp[j]) % mod
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()