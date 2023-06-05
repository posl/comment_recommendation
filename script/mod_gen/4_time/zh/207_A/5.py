def main():
    # 读取输入
    # 用空格分割读取的字符串，转换成整数
    # 用list保存输入的整数
    a, b, c = map(int, input().split())
    # 用list保存输入的整数
    cards = [a, b, c]
    # 用sum函数求和
    print(sum(cards))

if __name__ == '__main__':
    main()