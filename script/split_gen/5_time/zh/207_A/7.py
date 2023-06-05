def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 输出结果
    print(a + b + c - min(a, b, c))
