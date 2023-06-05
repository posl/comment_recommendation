def main():
    # 读取输入
    line = input()
    # 分割输入
    a, b, c = map(int, line.split())
    # 用列表来存储输入
    l = [a, b, c]
    # 用列表来存储不同的数字
    l2 = []
    # 用列表来存储相同的数字
    l3 = []
    # 用列表来存储最终结果
    l4 = []
    # 如果有两个相同的数字
    if l[0] == l[1] or l[1] == l[2] or l[2] == l[0]:
        # 遍历列表
        for i in l:
            # 如果列表中不存在该数字
            if i not in l2:
                # 将该数字添加到列表中
                l2.append(i)
            # 如果列表中存在该数字
            else:
                # 将该数字添加到列表中
                l3.append(i)
        # 遍历列表
        for i in l:
            # 如果i不在列表l3中
            if i not in l3:
                # 将i添加到列表l4中
                l4.append(i)
        # 遍历列表
        for i in l4:
            # 打印列表中的数字
            print(i)
    # 如果没有两个相同的数字
    else:
        # 打印0
        print(0)
