def main():
    # 读取数据
    n, m = map(int, input().split())
    # 创建二维数组
    a = [[0] * n for i in range(n)]
    # 创建一个数组
    b = [0] * n
    # 读取数据
    for i in range(m):
        k, *x = map(int, input().split())
        # 读取数据，创建二维数组
        for j in range(k):
            a[x[j] - 1][x[(j + 1) % k] - 1] = 1
            a[x[(j + 1) % k] - 1][x[j] - 1] = 1
    # 遍历数组
    for i in range(n):
        for j in range(n):
            # 如果a[i][j]为1
            if a[i][j] == 1:
                # b[i]加1
                b[i] += 1
    # 遍历数组
    for i in range(n):
        # 如果b[i]不为0
        if b[i] != 0:
            # 遍历数组
            for j in range(n):
                # 如果a[i][j]为1
                if a[i][j] == 1:
                    # b[j]加1
                    b[j] += 1
    # 遍历数组
    for i in range(n):
        # 如果b[i]为0
        if b[i] == 0:
            # 输出No
            print("No")
            # 退出程序
            exit()
    # 输出Yes
    print("Yes")

if __name__ == '__main__':
    main()