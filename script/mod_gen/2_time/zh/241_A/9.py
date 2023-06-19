def problem241_a():
    # 读取输入
    a = input().split(" ")
    # 转换成整数
    a = [int(i) for i in a]
    # 初始化
    k = 0
    # 循环3次
    for i in range(3):
        # 取出a_k
        k = a[k]
    # 输出
    print(k)

if __name__ == '__main__':
    problem241_a()