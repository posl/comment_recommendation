def main():
    # 读取输入
    x, y, d = map(int, input().split())
    # 计算
    # 旋转矩阵
    # x' = x * cos(d) - y * sin(d)
    # y' = x * sin(d) + y * cos(d)
    x1 = x * math.cos(math.radians(d)) - y * math.sin(math.radians(d))
    y1 = x * math.sin(math.radians(d)) + y * math.cos(math.radians(d))
    # 输出
    print(x1, y1)

if __name__ == '__main__':
    main()