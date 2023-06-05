def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算
    if (a + b) % 2 == 0:
        print("Easy")
    else:
        print("Hard")
