def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b =

if __name__ == '__main__':
    main()