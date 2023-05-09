def solve():
    # ナップサック問題
    # dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    # dp[i+1][w] = max(dp[i][w], dp[i][w-weight[i]] + value[i])
    n, w = map(int, input().split())
    dp = [[0]*(w+1) for _ in range(n+1)]
    for i in range(n):
        weight, value = map(int, input().split())
        for j in range(w+1):
            if j >= weight:
                dp[i+1][j] = max(dp[i][j], dp[i][j-weight] + value)
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])
solve()

if __name__ == '__main__':
    solve()