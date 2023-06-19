def main():
    # 读取输入
    # 读取一行
    line = input()
    # 读取一行，分割成两个变量
    a, b = map(int, input().split())
    # 读取一行，分割成两个变量，转换成整数
    c, d = map(int, input().split())
    # 打印输出
    print(a + b)
    print(c + d)

if __name__ == '__main__':
    main()