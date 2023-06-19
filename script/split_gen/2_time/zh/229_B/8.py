def main():
    # 读取输入
    a, b = map(int, input().split())
    # 处理
    if a + b >= 10:
        print("Hard")
    else:
        print("Easy")
