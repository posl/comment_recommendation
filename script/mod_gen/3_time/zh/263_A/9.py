def main():
    # 读取输入
    a, b, c, d, e = map(int, input().split())
    # 计算
    if a == b == c:
        if d == e:
            print("Yes")
        else:
            print("No")
    elif a == b == d:
        if c == e:
            print("Yes")
        else:
            print("No")
    elif a == b == e:
        if c == d:
            print("Yes")
        else:
            print("No")
    elif a == c == d:
        if b == e:
            print("Yes")
        else:
            print("No")
    elif a == c == e:
        if b == d:
            print("Yes")
        else:
            print("No")
    elif a == d == e:
        if b == c:
            print("Yes")
        else:
            print("No")
    elif b == c == d:
        if a == e:
            print("Yes")
        else:
            print("No")
    elif b == c == e:
        if a == d:
            print("Yes")
        else:
            print("No")
    elif b == d == e:
        if a == c:
            print("Yes")
        else:
            print("No")
    elif c == d == e:
        if a == b:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()