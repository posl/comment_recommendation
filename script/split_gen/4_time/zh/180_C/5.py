def main():
    # 读取输入
    N = int(input())
    # 初始化结果列表
    result = []
    # 遍历
    for i in range(1, int(N ** 0.5) + 1):
        # 如果可以整除
        if N % i == 0:
            # 加入结果
            result.append(i)
            # 如果不是平方数
            if N // i != i:
                # 加入结果
                result.append(N // i)
    # 排序
    result.sort()
    # 输出结果
    for i in result:
        print(i)
