def problem249_a():
    # 读取输入
    a, b, c, d, e, f, x = map(int, input().split())
    # 计算高桥和青木的跑步距离
    taka = (a + b) * c
    aoki = (d + e) * f
    # 判断谁跑得更远
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")
