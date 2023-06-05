def main():
    # 读取输入
    c1, c2, c3 = input().split()
    # 判断
    if c1 == c2 and c2 == c3:
        print("Won")
    else:
        print("Lost")
