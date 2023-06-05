def solve():
    # 读入数据
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # 累计时间
    t = 0
    # 累计通关次数
    ans = 0
    # 遍历阶段
    for a, b in AB:
        # 通关一次
        ans += 1
        # 累计时间
        t += a
        # 如果累计时间超过了限制
        if t > X:
            # 通关次数减去1
            ans -= 1
            # 结束循环
            break
        # 通关一次
        ans += 1
        # 累计时间
        t += b
    # 通关次数减去1
    ans -= 1
    # 输出答案
    print(ans)
solve()
