def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 逻辑处理
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

if __name__ == '__main__':
    main()