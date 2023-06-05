def main():
    # 读取输入
    n = int(input())
    # 问题求解
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            count += 1
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()