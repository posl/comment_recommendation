def main():
    import sys
    readline = sys.stdin.readline
    #N, W = map(int, input().split())
    N, W = map(int, readline().split())
    #AB = [list(map(int, input().split())) for _ in range(N)]
    AB = [list(map(int, readline().split())) for _ in range(N)]
    #dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for w in range(W+1):
            if w >= AB[i][1]:
                dp[i+1][w] = max(dp[i][w-AB[i][1]]+AB[i][0], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]
    print(dp[N][W])

if __name__ == '__main__':
    main()