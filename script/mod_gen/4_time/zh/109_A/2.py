def main():
    # 读取输入
    a, b = map(int, input().split())
    # 判断奇数
    if a * b % 2 == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()