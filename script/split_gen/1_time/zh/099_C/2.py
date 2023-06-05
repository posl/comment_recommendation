def solve(n):
    # 用来计算最小的次数
    ans = n
    # 9的次数
    i = 0
    while 9 ** i <= n:
        # 6的次数
        j = 0
        while 9 ** i + 6 ** j <= n:
            # 取最小值
            ans = min(ans, n - (9 ** i + 6 ** j) + i + j)
            j += 1
        i += 1
    return ans
