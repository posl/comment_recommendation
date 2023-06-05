def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 处理
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)
