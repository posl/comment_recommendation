def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    # dp[i][j] := i番目まで見たときに、jが最後になるような数列の数
    dp = [[0] * 3010 for _ in range(3010)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
    print(sum(dp[N]) % mod)

if __name__ == '__main__':
    main()