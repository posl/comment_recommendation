def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())
    # 写入代码
    if a3 - a2 == a2 - a1:
        print("Yes")
    else:
        print("No")
