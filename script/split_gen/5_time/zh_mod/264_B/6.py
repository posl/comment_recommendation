def main():
    # 输入
    r, c = map(int, input().split())
    # 输出
    if (r + c) % 2 == 0:
        print("black")
    else:
