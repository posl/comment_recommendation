def main():
    N = int(input())
    #dp[t][i] = t秒目に座標iにいる時の最大スコア
    dp = [[0]*5 for _ in range(10**5+1)]
    for _ in range(N):
        T, X, A = map(int, input().split())
        for i in range(5):
            if i == X:
                dp[T][i] = max(dp[T-1][i] + A, dp[T][i])
            else:
                dp[T][i] = max(dp[T-1][i], dp[T][i])
        for i in range(5):
            dp[T+1][i] = max(dp[T][i], dp[T+1][i])
    print(max(dp[-1]))

if __name__ == '__main__':
    main()