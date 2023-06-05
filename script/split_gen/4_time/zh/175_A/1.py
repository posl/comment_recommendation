def main():
    # 读取输入
    s = input()
    # 初始化
    count = 0
    max_count = 0
    # 计数
    for i in s:
        if i == "R":
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    # 打印最大值
    print(max_count)
