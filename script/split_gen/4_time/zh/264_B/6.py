def main():
    # 读取输入
    R, C = map(int, input().strip().split())
    # 处理
    if (R + C) % 2 == 0:
        print("黑色")
    else:
        print("白色")
