def main():
    snuke = []
    N = int(input())
    for i in range(N):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort(key=lambda x: x[0])
    # print(snuke)
    # dp[i][j]表示在第i个snuke的时候，高桥在第j个坑的最大收益
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            # 如果高桥在第i个snuke出现的时候，不在第j个坑，那么就把dp[i][j]设置为dp[i-1][j]
            if snuke[i][1] != j:
                dp[i + 1][j] = dp[i][j]
            # 如果高桥在第i个snuke出现的时候，就在第j个坑，那么就把dp[i][j]设置为dp[i-1][j-1]和dp[i-1][j+1]中的最大值
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - 1] + snuke[i][2], dp[i][j + 1] + snuke[i][2])
    # print(dp)
    print(dp[N][0])

if __name__ == '__main__':
    main()