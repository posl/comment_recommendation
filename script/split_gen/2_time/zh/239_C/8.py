def main():
    # 读取输入
    x1, y1, x2, y2 = map(int, input().split())
    # 判断是否满足条件
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")
