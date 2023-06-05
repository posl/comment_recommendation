def main():
    # 读取输入
    S = input()
    # 初始化
    count = 0
    max_count = 0
    # 遍历字符串
    for s in S:
        # 如果是R，计数加一
        if s == 'R':
            count += 1
        # 如果是S，计数归零
        else:
            count = 0
        # 更新最大值
        max_count = max(max_count, count)
    # 输出最大值
    print(max_count)
