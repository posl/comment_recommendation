def main():
    N, W = map(int, input().split())
    #dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        a, b = map(int, input().split())
        for w in range(W+1):
            if w-a >= 0:
                dp[i+1][w] = max(dp[i][w-a]+b, dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]
    print(dp[N][W])

if __name__ == '__main__':
    main()