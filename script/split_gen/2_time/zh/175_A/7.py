def main():
    # 读取输入
    S = input()
    # 计数器
    count = 0
    # 最大值
    max_count = 0
    # 遍历字符串
    for i in range(len(S)):
        # 如果是R
        if S[i] == "R":
            # 计数器加1
            count += 1
            # 如果计数器大于最大值
            if count > max_count:
                # 重新赋值最大值
                max_count = count
        # 如果不是R
        else:
            # 重置计数器
            count = 0
    # 输出最大值
    print(max_count)
