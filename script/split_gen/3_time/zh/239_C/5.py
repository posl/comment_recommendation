def main():
    # 读取输入
    x1, y1, x2, y2 = map(int, input().split())
    # 计算两点间的距离
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 判断距离是否等于根号5
    if dist == 5 ** 0.5:
        print("Yes")
    else:
        print("No")
