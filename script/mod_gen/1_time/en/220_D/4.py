def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for a in A:
            ndp = [0] * 10
            for j in range(10):
                ndp[(j+a)%10] += dp[j]
                ndp[(j+a)%10] %= mod
                ndp[(j*a)%10] += dp[j]
                ndp[(j*a)%10] %= mod
            dp = ndp
        ans[i] = dp[0]
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()