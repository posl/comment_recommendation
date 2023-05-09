def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    MOD = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]
            dp[i+1][j] %= MOD
        for j in range(B[i]+1, 3001):
            dp[i+1][j] = dp[i+1][j-1]
    print(dp[N][3000])

if __name__ == '__main__':
    main()