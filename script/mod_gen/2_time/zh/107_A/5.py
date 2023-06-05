def main():
    # 读取输入
    n, i = input().split()
    n = int(n)
    i = int(i)
    # 计算j
    j = n - i + 1
    # 输出结果
    print(j)

if __name__ == '__main__':
    main()