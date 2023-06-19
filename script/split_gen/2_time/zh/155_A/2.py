def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 逻辑处理
    if a == b and a != c:
        print("是")
    elif a == c and a != b:
        print("是")
    elif b == c and b != a:
        print("是")
    else:
        print("否")
