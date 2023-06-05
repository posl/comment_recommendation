def main():
    # 读入一行输入
    line = input()
    # 用空格分隔开来
    a = line.split()
    # 把每个数字转换成int类型
    a = list(map(int, a))
    # 求和
    s = sum(a)
    # 输出
    if s >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()