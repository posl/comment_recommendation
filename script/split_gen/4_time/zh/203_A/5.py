def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 检查是否有两个数字相同
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)
