def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if dp[i][j] == 0:
                continue
            for k in range(A[i], B[i]+1):
                if j > 0 and k < dp[i][j-1]:
                    continue
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= 998244353
    print(dp[N][N])

if __name__ == '__main__':
    main()