def main():
    # 读取数据
    with open('problems106_a.txt') as f:
        A, B = [int(i) for i in f.readline().split()]
    # 计算面积
    area = A * B - (A - 1) - (B - 1)
    # 输出结果
    print(area)
