def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = [[0 for _ in range(101)] for _ in range(n+1)]
    for i in range(n):
        for j in range(101):
            if j < c[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-c[i]]+v[i])
    print(dp[n][100])

if __name__ == '__main__':
    main()