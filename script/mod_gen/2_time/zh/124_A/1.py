def problems124_a():
    # 读取两个整数
    A, B = map(int, input().split())
    # 用列表存储两个按钮的值
    list = [A, B]
    # 用列表存储按两次按钮的结果
    list2 = []
    # 用for循环遍历两个按钮的值
    for i in range(len(list)):
        # 用while循环计算按两次按钮的结果
        while list[i] > 0:
            # 按两次按钮的结果
            list2.append(list[i])
            # 按一次按钮的结果
            list[i] -= 1
    # 输出按两次按钮的结果之和
    print(sum(list2))
problems124_a()
