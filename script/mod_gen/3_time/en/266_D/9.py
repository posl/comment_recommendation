def main():
    N = int(input())
    info = []
    for i in range(N):
        info.append(list(map(int, input().split())))
    info.sort()
    dp = [[0] * 5 for _ in range(100005)]
    for i in range(N):
        t, x, a = info[i]
        for j in range(5):
            dp[t][j] = max(dp[t][j], dp[t - 1][j])
        dp[t][x] = max(dp[t][x], dp[t - 1][x] + a)
    print(max(dp[-1]))

if __name__ == '__main__':
    main()