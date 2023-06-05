def main():
    # 读取输入
    line = input().split()
    # 转换为整数
    a = int(line[0])
    b = int(line[1])
    # 求最大值
    if a > b:
        print(a + max(a - 1, b))
    else:
        print(b + max(a, b - 1))
