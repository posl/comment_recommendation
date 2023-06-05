def main():
    # 读取输入
    x,y,z = map(int, input().split())
    # 交换
    a = x
    x = y
    y = a
    # 交换
    b = x
    x = z
    z = b
    # 输出
    print(x,y,z)
