def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [0] * (sum(a) + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(len(dp) - 1, -1, -1):
            if j - a[i] >= 0:
                dp[j] += dp[j - a[i]]
                dp[j] %= mod
    #print(dp)
    ans = 0
    for i in range(1, len(dp)):
        if dp[i] != 0 and dp[i] % 2 == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()