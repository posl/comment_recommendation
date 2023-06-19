def main():
    # 读取输入
    D, T, S = map(int, input().split())
    # 判断
    if T * S >= D:
        print("Yes")
    else:
        print("No")
