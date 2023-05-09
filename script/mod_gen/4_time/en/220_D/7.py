def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(N):
            next = [0] * 10
            for k in range(10):
                next[(k + A[j]) % 10] += dp[k]
                next[(k * A[j]) % 10] += dp[k]
            dp = next
        ans[i] = dp[0]
    print("\n".join(map(str, ans)))

if __name__ == '__main__':
    main()