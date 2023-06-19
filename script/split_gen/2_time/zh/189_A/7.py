def main():
    # 读入一行
    line = input()
    # 用空格分割
    line = line.split()
    # 取第一个元素
    c1 = line[0]
    # 取第二个元素
    c2 = line[1]
    # 取第三个元素
    c3 = line[2]
    # 如果这三个元素相同
    if c1 == c2 and c2 == c3:
        # 打印Won
        print("Won")
    # 否则
    else:
        # 打印Lost
        print("Lost")
