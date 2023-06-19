def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 求解并输出
    print(max(0, c - (a - b)))
