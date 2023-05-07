def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * 5 for _ in range(n + 1)]
    for i in range(n):
        for j in range(5):
            if j == s[i][1]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j] + s[i][2])
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - 1] + s[i][2])
    print(max(dp[-1]))

if __name__ == '__main__':
    main()