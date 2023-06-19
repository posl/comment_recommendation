def main():
    # 从标准输入读取整数
    # 用map函数将输入的整数分成三个变量
    x, y, z = map(int, input().split())
    # 输出三个变量
    print(z, x, y)

if __name__ == '__main__':
    main()