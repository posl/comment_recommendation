def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] = i番目までの数列で、最後の要素がjのときの個数
    dp = [[0] * (3001) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            dp[i + 1][j] = (dp[i + 1][j] + dp[i + 1][j - 1]) % MOD
    print(dp[N][B[-1]])

if __name__ == '__main__':
    main()