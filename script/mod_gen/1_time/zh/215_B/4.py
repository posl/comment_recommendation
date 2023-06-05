def main():
    # 读取输入
    n = int(input())
    # 计算结果
    k = 0
    while 2 ** k <= n:
        k += 1
    # 输出结果
    print(k - 1)

if __name__ == '__main__':
    main()