def main():
    # Get input here
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        a, b = map(int, input().split())
        cheese.append((a, b))
    # Solve problems
    # Sort cheese by deliciousness
    cheese.sort(key=lambda x: x[0])
    # print(cheese)
    # dp[i][j]: Max deliciousness using i items and j grams of cheese
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(W + 1):
            if j - cheese[i - 1][1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cheese[i - 1][1]] + cheese[i - 1][0])
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    # Get output here
    print(dp[N][W])

if __name__ == '__main__':
    main()