def main():
    N = int(input())
    X = []
    T = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        X.append(x)
        T.append(t)
        A.append(a)
    dp = [[0 for j in range(5)] for i in range(N)]
    for i in range(N):
        for j in range(5):
            if i == 0:
                if X[i] == j:
                    dp[i][j] = A[i]
            else:
                dp[i][j] = dp[i-1][j]
                if X[i] == j:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + A[i])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + A[i])
                if j < 4:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1] + A[i])
    print(max(dp[N-1]))

if __name__ == '__main__':
    main()