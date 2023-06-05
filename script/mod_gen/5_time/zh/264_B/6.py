def main():
    # 读取输入
    line = input().split()
    # 转换为整数
    r = int(line[0])
    c = int(line[1])
    # 如果行列均为偶数，输出黑色
    if r % 2 == 0 and c % 2 == 0:
        print("black")
    # 如果行列均为奇数，输出黑色
    elif r % 2 == 1 and c % 2 == 1:
        print("black")
    # 否则输出白色
    else:
        print("white")

if __name__ == '__main__':
    main()