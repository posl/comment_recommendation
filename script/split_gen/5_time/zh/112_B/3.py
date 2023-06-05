def input():
    # 读取输入
    # 读取整数n和t
    line = input().split()
    n = int(line[0])
    t = int(line[1])
    # 读取n行
    routes = []
    for i in range(n):
        line = input().split()
        routes.append([int(line[0]), int(line[1])])
    return n, t, routes
