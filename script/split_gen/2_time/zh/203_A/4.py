def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 处理
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)
