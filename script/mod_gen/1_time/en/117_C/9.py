def main():
    #input
    N, M = map(int, input().split())
    Xs = list(map(int, input().split()))
    Xs.sort()
    #compute
    #dp[i][j] := i番目のピースをj番目のXsに移動させるまでの最小コスト
    dp = [[float('inf')] * M for _ in range(N)]
    for j in range(M):
        dp[0][j] = abs(Xs[j] - Xs[0])
    for i in range(1, N):
        for j in range(i, M):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(Xs[j] - Xs[j-i]))
    #output
    print(dp[-1][-1])

if __name__ == '__main__':
    main()