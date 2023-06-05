def main():
    # 读取输入
    line = input()
    # 用空格分隔输入
    A, B, C, D, E, F = map(int, line.split())
    # 计算结果
    result = A * B * C - D * E * F
    # 打印结果
    print(result % 998244353)

if __name__ == '__main__':
    main()