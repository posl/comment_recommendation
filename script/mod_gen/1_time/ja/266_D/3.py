def main():
    N = int(input())
    data = []
    for _ in range(N):
        T, X, A = map(int, input().split())
        data.append([T, X, A])
    ans = 0
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            if j != data[i][1]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + data[i][2])
            if abs(j - data[i][1]) <= data[i][0] - i:
                dp[i + 1][data[i][1]] = max(dp[i + 1][data[i][1]], dp[i][j])
        ans = max(ans, max(dp[i + 1]))
    print(ans)

if __name__ == '__main__':
    main()