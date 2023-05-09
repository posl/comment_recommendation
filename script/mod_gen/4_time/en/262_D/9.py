def main():
    n = int(input())
    a = list(map(int, input().split()))
    # dp[i] = (i個の要素の和, i個の要素の数)の組み合わせの数
    dp = [0] * (n + 1)
    dp[0] = (0, 1)
    for i in range(n):
        for j in range(i, -1, -1):
            x, y = dp[j]
            dp[j + 1] = (x + a[i] * y, y)
    ans = 0
    for i in range(1, n + 1):
        x, y = dp[i]
        if x % y == 0:
            ans += pow(2, n - i, 998244353) * y
            ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()