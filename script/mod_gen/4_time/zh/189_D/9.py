def solve():
    # 读入数据
    N = int(input())
    S = [input() for _ in range(N)]
    # 状态压缩
    # 0: False, 1: True
    # 0: AND, 1: OR
    # 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5
    # 0: 00, 1: 01, 2: 10, 3: 11
    # 0: 000, 1: 001, 2: 010, 3: 011, 4: 100, 5: 101, 6: 110, 7: 111
    dp = [[0] * 8 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        if S[i - 1] == 'AND':
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
            dp[i][2] = dp[i - 1][2] + dp[i - 1][0]
            dp[i][3] = dp[i - 1][3] + dp[i - 1][1]
            dp[i][4] = dp[i - 1][4] + dp[i - 1][2]
            dp[i][5] = dp[i - 1][5] + dp[i - 1][3]
            dp[i][6] = dp[i - 1][6] + dp[i - 1][4]
            dp[i][7] = dp[i - 1][7] + dp[i - 1][5]
        else:
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][1]
            dp[i][2] = dp[i - 1][2] + dp[i - 1][0]
            dp[i][3] = dp[i - 1][3] + dp[i - 1][1]
            dp[i][4] = dp

if __name__ == '__main__':
    solve()