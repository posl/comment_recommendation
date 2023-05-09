def main():
    import sys
    readline = sys.stdin.readline
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    #dp[i][j]: i番目の要素までで、j個のグループに分割する時の最小値
    dp = [[10**9]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N+1):
            if dp[i][j] == 10**9:
                continue
            for k in range(K+1):
                if i+k > N:
                    break
                dp[i+k][j+1] = min(dp[i+k][j+1], max(dp[i][j], A[i+k-1]))
    ans = 10**9
    for i in range(N+1):
        ans = min(ans, dp[N][i])
    print(ans)

if __name__ == '__main__':
    main()