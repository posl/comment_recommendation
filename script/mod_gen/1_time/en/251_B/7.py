def main():
    #input
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    #algorithm
    A.sort()
    A = [0] + A
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j - A[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]] + A[i])
            else:
                dp[i][j] = dp[i-1][j]
    #output
    print(sum(dp[N]))

if __name__ == '__main__':
    main()