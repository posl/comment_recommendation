def main():
    # 读取输入
    line = input()
    # 分割输入，得到三条边的长度
    values = line.split()
    # 将三条边的长度转换为整数
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    # 计算面积
    area = a * b // 2
    # 输出面积
    print(area)
