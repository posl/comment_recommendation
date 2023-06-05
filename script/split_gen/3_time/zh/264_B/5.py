def main():
    # 读取输入
    R, C = map(int, input().split())
    # print(R, C)
    # 判断
    if R % 2 == 0:
        if C % 2 == 0:
            print("白色")
        else:
            print("黑色")
    else:
        if C % 2 == 0:
            print("黑色")
        else:
            print("白色")
