def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算和
    print(a + b + c - min(a, b, c))
