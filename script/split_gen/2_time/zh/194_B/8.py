def find_min_time():
    # 读取输入数据
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # 计算最短时间
    min_time = max(a[0], b[0])
    for i in range(1, n):
        time = max(a[i], b[i])
        if time < min_time:
            min_time = time
    # 输出结果
    print(min_time)
