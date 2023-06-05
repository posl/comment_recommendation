def main():
    # 读取输入
    A, B = map(int, input().split())
    #初始化计数器
    count = 0
    # 遍历整数
    for i in range(A, B + 1):
        # 如果是整数，计数器加1
        count += 1
    # 打印计数器
    print(count)
