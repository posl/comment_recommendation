def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if a == b:
        if a == c:
            print("否")
        else:
            print("是")
    elif b == c:
        print("是")
    elif a == c:
        print("是")
    else:
        print("否")
