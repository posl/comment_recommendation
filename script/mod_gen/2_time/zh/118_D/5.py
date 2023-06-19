def get_max_number(n, m, a):
    # 用来组成数字1，2，3，4，5，6，7，8，9的火柴棒数量
    match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    match_dict = {}
    for i in range(m):
        match_dict[a[i]] = match[i]
    # 定义dp数组，dp[i]表示用i根火柴棒能组成的最大整数
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i >= match_dict[a[j]] and dp[i - match_dict[a[j]]] != -1:
                dp[i] = max(dp[i], dp[i - match_dict[a[j]]] * 10 + int(a[j]))
    return dp[n]

if __name__ == '__main__':
    get_max_number()