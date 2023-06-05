def main():
    a = input("请输入第一个数：")
    b = input("请输入第二个数：")
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if a >= 1 and a <= 20 and b >= 1 and b <= 20:
            print(a * b)
        else:
            print("输入的数不在范围内")
    else:
        print("输入的不是整数")

if __name__ == '__main__':
    main()