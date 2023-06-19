def main():
    # 读取输入
    abc = input().split()
    # 转换为整数
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    # 计算面积
    s = a * b / 2
    # 输出结果
    print(int(s))

if __name__ == '__main__':
    main()