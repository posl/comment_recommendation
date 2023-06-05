def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 逻辑处理 & 结果输出
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif a == c:
        print(b)
    else:
        print(0)
