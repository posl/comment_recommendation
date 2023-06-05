def main():
    # 获取输入内容
    q = int(input())
    # 定义列表
    a = [-1 for i in range(2 ** 20)]
    # 循环处理输入内容
    for i in range(q):
        # 获取输入内容
        t, x = map(int, input().split())
        # 判断输入内容
        if t == 1:
            # 定义变量
            h = x
            # 循环处理
            while a[h % (2 ** 20)] != -1:
                h += 1
            # 定义变量
            a[h % (2 ** 20)] = x
        else:
            # 输出结果
            print(a[x % (2 ** 20)])

if __name__ == '__main__':
    main()