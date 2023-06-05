def main():
    # 读入数据
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # 初始化dp数组
    dp = [[0]*3 for i in range(N)]
    # 初始化dp数组的第一行
    if T[0] == 'r':
        dp[0][1] = P
        dp[0][2] = S
    elif T[0] == 's':
        dp[0][0] = R
        dp[0][2] = S
    else:
        dp[0][0] = R
        dp[0][1] = P
    # 递推
    for i in range(1, N):
        if T[i] == 'r':
            dp[i][0] = max(dp[i-1][1], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + P
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        elif T[i] == 's':
            dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + R
            dp[i][1] = max(dp[i-1][0], dp[i-1][2])
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        else:
            dp[i][0] = max(dp[i-1][1], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + S
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        if i >= K:
            dp[i][0] = max(dp[i][0], dp[i-K][0])
            dp[i][1] = max(dp[i][1], dp[i-K][1])
            dp[i][2] = max(dp[i][2], dp[i-K][2])
    # 打印结果
    print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

if __name__ == '__main__':
    main()