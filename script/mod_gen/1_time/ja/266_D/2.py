def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    # dp[i][j] = i番目のすぬけ君を捕まえる時の最大値
    dp = [[0 for j in range(5)] for i in range(N+1)]
    for i in range(N):
        for j in range(5):
            if T[i] < i+1:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][X[i]] + A[i])
    print(max(dp[N]))

if __name__ == '__main__':
    main()