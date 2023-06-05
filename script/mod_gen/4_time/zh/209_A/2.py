def main():
    a = int(input("输入a:"))
    b = int(input("输入b:"))
    if a < 1 or a > 100 or b < 1 or b > 100:
        print("输入的a,b不在范围内")
        return
    if a > b:
        print("输入的a大于b,不符合要求")
        return
    print(b - a + 1)

if __name__ == '__main__':
    main()