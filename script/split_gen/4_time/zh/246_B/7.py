def main():
    # 读入数据
    A, B = map(int, input().split())
    # 计算结果
    x = A / (A ** 2 + B ** 2) ** 0.5
    y = B / (A ** 2 + B ** 2) ** 0.5
    # 输出结果
    print(x, y)
    # print("{:.12f} {:.12f}".format(x, y))
