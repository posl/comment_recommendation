def main():
    # 读入数据
    n, t = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(n)]
    # print(ct)
    # 用于保存结果
    result = 1001
    # 遍历所有的路线
    for c, t_ in ct:
        # 如果时间不超过限制
        if t_ <= t:
            # 更新结果
            result = min(result, c)
    # 如果结果没有更新
    if result == 1001:
        # 打印TLE
        print('TLE')
    # 否则
    else:
        # 打印结果
        print(result)

if __name__ == '__main__':
    main()