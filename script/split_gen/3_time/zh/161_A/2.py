def main():
    # 读取输入
    x, y, z = map(int, input().split())
    # 交换
    tmp = x
    x = y
    y = tmp
    # 交换
    tmp = x
    x = z
    z = tmp
    # 打印
    print(x, y, z)
